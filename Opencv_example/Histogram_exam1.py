import numpy as np, cv2


def calc_histo(iimagem, hsize, ranges=[0, 256]):
    hist = np.zeros((hsize, 1), np.float)
    gap = ranges[1] / hsize

    for i in (image / gap).flat :
        hist[int(i)] += 1
        return hist

    image = cv2.imread("images/pixek.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("영상 파일 읽기 오류 발생")

    hsize, ranges = [32], [0, 256]
    gap = ranges[1] / hsize
    ranges_gap = np.arange(0, ranges[1] + 1, gap)
    hist1 = calc_histo(image, hsize[0], ranges)
    hist2 = cv2.calcHist([image], 0, None, hsize, ranges)
    hist3, bins = np.histogram(image, ranges_gap)

    print("User 함수 : \n", hist1.flatten())
    print("OpenCV 함수 : \n", hist2.flatten())
    print("numpy 함수 : \n", hist3)

    cv2.imshow("image", image)
    cv2.waitKey(0)
