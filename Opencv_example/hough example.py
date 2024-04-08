import numpy as np, cv2, math

def accumulate(image, rho, theta):
    h, w = image.shape[:2]
    rows, cols = (h + w) * 2 // rho, int( np.pi/theta)  # 누적행렬 너비, 높이
    accumulate = np.zeros((rows, cols), np.int32)    # 직선 누적행렬

    sin_cos = [(np.sin(t * theta), np.cos(t * theta)) for t in range(cols)]  # 삼각 함수값 미리 저장
    # pts = [(y, x) for x in range(w) for y in range(h) if image[y, x] > 0 ]
    pts = np.where(image > 0)

    polars = np.dot(sin_cos, pts).T            # 행렬곱으로 허프 변환 수식 계산
    polars = (polars/ rho + rows / 2)           # 해상도 변경 및 위치 조정

    for row in polars.astype(int):
       for t, r in enumerate(row):
          accumulate[r, t] += 1                     # 좌표 누적

    return accumulate

# 허프 누적 행렬의 지역 최대값 선정
def masking(accumulate, h, w, thresh):
    rows, cols = accumulate.shape[:2]
    dst = np.zeros(accumulate.shape, np.uint32)

    for y in range(0, rows, h):             # 누적행렬 조회
        for x in range(0, cols, w):
            roi = accumulate[y:y+h, x:x+w]
            _ , max, _, (x0, y0) = cv2.minMaxLoc(roi)
            dst[y+y0, x+x0] = max
    return dst

        # 임계값 이상인 누적값(직선) 선별
def select_lines(acc_dst, rho, theta, thresh):
    rows = acc_dst.shape[0]
    r, t = np.where(acc_dst>thresh)             # 임계값 이상인 좌표(세로, 가로)

    rhos = ((r - (rows / 2)) * rho)             # rho 계산
    radians = t * theta                          # theta 계산
    value = acc_dst[r,t]                        # 임계값 이상인 누적값

    idx = np.argsort(value)[::-1]       # 누적값 기준 세로 방향 내림차순 정렬
    lines = np.transpose([rhos, radians])        # ndarray 객체 생성후 전치
    lines = lines[idx, :]                          # 누적값에 다른 정렬

    return np.expand_dims(lines, axis=1)


# 허프 변환
def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)  # 허프 누적 행렬 계산
    acc_dst = masking(acc_mat, 7, 3, thresh)  # 마스킹 처리 7행,3열
    lines   = select_lines(acc_dst, rho, theta, thresh)  # 직선 가져오기
    return lines

image = cv2.imread('../image/hough.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
canny = cv2.Canny(image, 100, 200, 5)

rho, theta = 1,  np.pi / 180
lines = cv2.HoughLines(canny, 1, np.pi/180, 130)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.waitKey(0)