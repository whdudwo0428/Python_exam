import numpy as np
import cv2


def onChange(value): #함수만들때는 무조건 : def 함수이름(인자)
    global image #전역변수로  image선언

    add_value = value - int(image[0][0]) #트랙바 값과 영상 화소값 차분
    print("추가 화소값:", add_value)

    image[:] = image + add_value    #행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)


image = np.zeros((300, 500), np.uint8) #영상 생성

title = 'Trackerbar Event'
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange) #image[0][0]: onChange함수값 입력값 / 255는 최댓값
cv2.waitKey(0)
cv2.destroyAllWindows(title)
