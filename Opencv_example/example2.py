import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8) #uint8:unsinged 2^8:256
image.fill(255) #흰색

title1, title2 = 'AUTOSIZE', 'NORMAL' #title 이름을 정해줌
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image) #창을 띄우는거
cv2.imshow(title2, image)
cv2.resizeWindow(title1,400,300)
cv2.resizeWindow(title2,400,300)
cv2.waitKey(0) #입력을 받을때까지 몇초나 기다릴건가
cv2.destroyAllWindows() #창을 끄기위한거 저절로 지금은 안넣어도됨
