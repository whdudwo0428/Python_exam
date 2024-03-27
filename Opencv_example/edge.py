import numpy as np, cv2 # 아직 코드수정 x


# shift Tap 하면 탭단위로 땡겨짐
# 회선 수행 함수 - 행렬 처리 방식(속도 면에서 유리)
def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)  # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1] // 2, mask.shape[0] // 2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1  # 관심영역 높이 범위
            x1, x2 = j - ycenter, i + ycenter + 1  # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32")  # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)  # 회선 적용-OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]
    return dst


def differential(image, date1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2)
    dst1, dst2 = np.abs(dst1), np.abs(dst2)

    dst = np.clip(dst, 0, 255).astype("uint8")
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")
    return dst, dst1, dst2


image = cv2.imread("../image/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0,1,
         -1, 1, 1,
         -1, 0, 0]
data2 = [-1, -1, -1,
         0, 0, 0,
         1, 1, 1]
dst, dst1, dst2 = differential(image, data1, data2)

cv2.imshow("image", image)
cv2.imshow("robers edge", dst)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)
