import numpy as np, cv2


# 문자열 출력 함수 - 그림자 효과
def put_string(frame, text, pt, value=None, color=(120, 200, 90)):
    text = str(text) + str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, color, 2)  # 작성 문자


def cornerHarris(img, ksize, k):
    dx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize)  # 수직 소벨 마스크
    dy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize)  # 수평 소벨 마스크

    a = cv2.GaussianBlur(dx * dx, (5, 5), 0)  # 가우시안 블러링 수행
    b = cv2.GaussianBlur(dy * dy, (5, 5), 0)
    c = cv2.GaussianBlur(dx * dy, (5, 5), 0)

    corner = (a * b - c * c) - k * (a + b) ** 2  # 코너 응답 함수 계산 -행렬 연산 적용
    return corner


def drawCorner(corner, image, thresh):
    corner = cv2.normalize(corner, 0, 300, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    pts = np.where(corner > thresh)
    h, w = corner.shape
    corners = []
    for j, i in np.transpose(pts):
        if 0 < i < h - 1 and 0 < j < w - 1:
            neighbor = corner[i - 1:i + 2, j - 1:j + 2].flatten()
            max = np.max(neighbor[1::2])
            if corner[i, j] >= max: corners.append((j, i))

    for pt in corners:
        cv2.circle(image, pt, 3, (0, 230, 0), -1)  # 좌표 표시
    print("임계값: %2d , 코너 개수: %2d" % (thresh, len(corners)))
    return image


def onCornerHarris(thr):
    img1 = drawCorner(corner1, np.copy(image), thr)
    img2 = drawCorner(corner2, np.copy(image), thr)

    put_string(img1, "USER", (10, 30), "")
    put_string(img2, "OpenCV", (10, 30), "")
    dst = cv2.repeat(img1, 1, 2)  # 두 개 영상을 하나의 윈도우에 표시
    dst[:, img1.shape[1]:, :] = img2
    cv2.imshow("harris detect", dst)


image = cv2.imread('../image/harris.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

blockSize, apertureSize = 4, 3  # 소벨 마스크 크기
k, thresh = 0.04, 2  # 코너 응답 임계값
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
corner1 = cornerHarris(gray, apertureSize, k)  # 사용자 정의 함수
corner2 = cv2.cornerHarris(gray, blockSize, apertureSize, k)  # OpenCV 제공 함수
cv2.namedWindow('harris detect')
cv2.createTrackbar("Threshold", "harris detect", thresh, 20, onCornerHarris)
cv2.waitKey(0)
