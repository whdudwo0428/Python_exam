import numpy as np, cv2


def calc_histo(image, hsize, ranges=[0, 256]):
    # calc_histo(image,hsize) :  미리 초기값을 정해주고 사용자가 정해주지 않으면 이 범위가 들어간다
    hist = np.zeros((hsize, 1), np.float)
    gap = ranges[1] / hsize

    for i in (image / gap).flat:
        hist[int(i)] += 1
        return hist


def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0])
    gap = hist_img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        roi = (x, 0, w, int(h))
        cv2.rectangle(hist_img, roi, 150, -1)
        cv2.rectangle(hist_img, roi, 0, 1)

    return cv2.flip(hist_img, 0)


image = cv2.imread("../image/pixel.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

hist = cv2.calcHist([image], [0], None, [32], [0, 256])
hist_img = draw_histo(hist)

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.waitKey(0)
