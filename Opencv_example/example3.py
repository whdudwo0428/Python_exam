import numpy as np
import cv2

switch_case = {
    ord('a'): "a키 입력",
    ord('b'): "b키 입력",
    0x41: "a키 입력",
    int('0x41', 16): "b키 입력",
    2424832: "왼쪽 화살표키 입력",
    2424832: "윗쪽 화살표키 입력",
    2424832: "오른쪽 화살표키 입력",
    2424832: "아래쪽 화살표키 입력"
}

image = np.ones((200, 300), np.float64)
cv2.namedWindow("Keyboard Event")  #
cv2.imshow("Keyboard Event", image)
while True:
    key = cv2.waitKeyEx(100)
    if key == 27: break #27은  esc키다 유명하고 자주쓰는건 외우게 됨

    try:
        result = switch_case[key] #키번호 말해줌
        print(result)
    except KeyError:
        result = -1 #아니면 -1 출력

cv2.destroyAllWindows()  # 창을 끄기위한거 저절로 지금은 안넣어도됨

#ctrl alt l 누르면 자리 맞춰짐