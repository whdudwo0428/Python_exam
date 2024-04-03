import numpy as np
import cv2

title1 = "imread Test"
image = cv2.imread('../image/read_color.jpg') #imread 이미지읽어올때 사용
if image is None: 
    print("파일 읽기 오류")
#3은 채널을 의미함
cv2.imshow(title1, image)
cv2.waitKey(0)

# file setting plugin image 우클릭하고  view as image누르면 미리보기 씹가능 간단한 편집 가능
