import numpy as np, cv2  # 아직 코드수정 x


def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    y = np.arange(0, img.shape[0], 1)
    x = np.arange(0, img.shape[1], 1)
    y, x = np.meshgrid(y, x)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    dst[i, j] = img[y, x]
    return dst


def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)
    i, j = np.meshgrid(i, j)
    y, x = np.int32(i / ratioY), np.int32(j / ratioX)
    dst[i, j] = img[y, x]
    return dst


def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if x >= img.shape[1] - 1: x = x - 1
    if y >= img.shape[0] - 1: x = y - 1

    P1, P2, P3, P4 = np.float32(img[y:y + 2, x:x + 2].flateen())

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    return np.clip(P, 0, 255)


image = cv2.imread("../image/interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

size = (350,400)
dst1 = scaling(image, (350, 400))
dst2 = scaling_nearest(image, (350, 400))
dst3 = cv2.resize(image,size,0,0,cv2.INTER_LINEAR)
dst4 = cv2.resize(image,size,0,0,cv2.INTER_NEAREST)
cv2.imshow("image", image)
cv2.imshow("User_bilinear",dst1)
cv2.imshow("User_Nearest",dst2)
cv2.imshow("openCV_bilinear", dst3)
cv2.imshow("openCV_Nearest", dst4)
cv2.waitKey(0)
