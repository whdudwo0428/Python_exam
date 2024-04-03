import numpy as np
import cv2

capture = cv2.VideoCapture("../image/video_file.avi")  #확장자비디코 코덱을 분석해서 불러오는 역할
'''
파일을 열때 상대경로와 절대경로가 있다
../~~  내 디렉토리보다 위에 있을경우
./~~ 내 디렉토리와 같은 곳에 있을 때
'''
if not capture.isOpened(): raise Exception("동영상 파일 개방 안됨") #열렸나 물어봤느데 아니다 파일없다 대답

frame_rate = capture.get(cv2.CAP_PROP_FPS)*3 #PROP: property특징중에 _ FPS를 가져온다 뒤에 *n하면 배속
delay = int(1000 / frame_rate) #1000밀리s 한장을 몇초에 한장씩 보여줄거냐
frame_cnt = 0

while True:
    ret, frame = capture.read() #capture.read할때마다 frame1,2,3,4 .... 한장읽어오고 한장읽어오고
    if not ret or cv2.waitKey(delay) >= 0: break  # 키를 입력하면 꺼짐
    blue, green, red = cv2.split(frame) #fram에서 rgb값 분할
    frame_cnt += 1

    if 100 <= frame_cnt < 200: #프레임값이 범위 지날때마다
        cv2.add(blue, 100, blue) #파랑이를 더 파랑으로
    elif 200 <= frame_cnt < 300:
        cv2.add(green, 100, green) #초록을 더 초록으로
    elif 300 <= frame_cnt < 400:
        cv2.add(red, 100, red) #빨강이를 더 빨강으로
# add()
    frame = cv2.merge([blue, green, red]) # 다합쳐서 원래 이미지로 바꿔줌
    cv2.imshow("READ VIDEO FILE", frame)

capture.release()
