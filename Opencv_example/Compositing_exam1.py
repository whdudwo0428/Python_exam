import numpy as np, cv2

image1 = cv2.imread("../image/add1.jpg", cv2.IMREAD_GRAYSCALE)    #영상 읽기
image2 = cv2.imread("../image/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")

#영상합성
alpha, beta = 0.6, 0.7
add_img1 = cv2.add(image1, image2)                                  #곱셈 비율
add_img2 = cv2.add(image1 * alpha, image2 * beta)                   # 두 영상 단순 더하기
add_img2 = np.clip(add_img2, 0, 255).astype("uint8")                # 두 영상 비율에 따른 더하기
            # clip:내가 상한선과 하한선을 정해주고 어떤 값이 오버되거나 모자르면 범위에 맞춰주는 거
add_img3 = cv2.addWeighted(image1, alpha, image2, beta, 0)          # saturation 처리

titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey(0)
