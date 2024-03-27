import numpy as np, cv2

BRG_image = cv2.imread("../image/color_model.jpg", cv2.IMREAD_COLOR)  # 컬러영상읽기
if BRG_image is None: raise Exception("영상파일 읽기 오류")

white = np.array([255, 255, 255], np.uint8)
CMY_img = white - BRG_image
CMY = cv2.split(CMY_img)  # 채널분리

black = cv2.min(CMY[0], cv2.min(CMY[1], CMY[2]))  # 원소 간의 최솟값 저장
Yellow, Magenta, Cyan = CMY - black

titles = ['black', 'Yellow', 'Magenta', 'Cyan']
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)
