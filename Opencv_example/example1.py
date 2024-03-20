import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8) #uint8:unsinged 2^8:256
image[:] = 200 #밝은 검정? 회색

title1, title2 = 'Position1', 'Position2' #title 이름을 1,2로 정해줌
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) #window_size를 200,400으로 정할거
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150) #창 뜨는 위치 정해줌 (좌표)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image) #창을 띄우는거
cv2.imshow(title2, image)
cv2.waitKey(0) #입력을 받을때까지 몇초나 기다릴건가
cv2.destroyAllWindows() #창을 끄기위한거 저절로 지금은 안넣어도됨
