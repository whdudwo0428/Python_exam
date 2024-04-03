import numpy as np, cv2  # 아직 코드수정 x


def nonmax_suppression(sobel, direct):
    rows, cols, = sobel.shape[:2]
    dst = np.zeros((rows, cols), np.float32)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            values = sobel[i - 1:i + 2, j - 1, j + 2].flatten()
            first = [3, 0, 1, 2]
            id = first[direct[i, j]]
            v1, v2 = values[id], values[8 - id]

            dst[i, 2] = sobel[i, j] if (v1 < sobel[i, j] > v2) else 0
        return dst


def trace(max_sobel, i, j, low):
    h, w = max_sobel.shape
    if (0 <= i < h and 0 <= j < w) == False: return
    if pos_ck[i, j] == 0 and max_sobel[i, j] > low:
        pos_ck[i, j] = 255
        canny[i, j] = 255

    trace(max_sobel, i - 1, j - 1, low)
    trace(max_sobel, i, j - 1, low)
    trace(max_sobel, i + 1, j - 1, low)
    trace(max_sobel, i - 1, j, low)
    trace(max_sobel, i + 1, j, low)
    trace(max_sobel, i - 1, j + 1, low)
    trace(max_sobel, i, j + 1, low)
    trace(max_sobel, i + 1, j + 1, low)


def hystersesis_th(max_sobel, low, high):
    rows,cols = max_sobel.shape[:2]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if max_sobel[i,j]> high: trace(max_sobel,i,j,low)

image=cv2.imread("../image/canny.jpg",cv2.IMREAD_GRAYSCALE)
if image is None : raise Exception("영상파일 읽기 오류")

pos_ck=np.zeros(image.shape[:2],np.uint8)
canny=np.zeros(image.shape[:2],np.uint8)

gaus_img = cv2.GaussianBlur(image,(5,5),0.3)
Gx = cv2.Sobel(np.float32(gaus_img),cv2.CV_32F,1,0,3)
Gy = cv2.Sobel(np.float32(gaus_img),cv2.CV_32F,0,1,3)
sobel= cv2.magnitude(Gx,Gy)

directs = cv2.phase(Gx,Gy)/(np.pi/4)
directs = directs.astype(int)%4

max_sobel = nonmax_suppression(sobel,directs)

hystersesis_th(max_sobel,100,150)
canny2=cv2.Canny(image,100,150)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("OpenCV_Canny", canny2)
cv2.waitKey(0)