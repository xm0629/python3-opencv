import numpy as np
import cv2 as cv


def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_path = '/home/xm/repository/xm-mathpy/opencv/haarcascades/haarcascade_frontalface_default.xml'
    face_detector = cv.CascadeClassifier(face_path)

    face = face_detector.detectMultiScale(gray, 1.02, 19)
    for x, y, w, h in face:
        cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv.imshow('result', image)




print('----------Hello Python----------')
#src = cv.imread('./figure/girls.jpg')
capture = cv.VideoCapture(0)
# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.namedWindow('result', cv.WINDOW_AUTOSIZE)
while True:
    ret, frame = capture.read()
    frame = cv.flip(frame, 1)
    face_detect_demo(frame)
    c = cv.waitKey(10)
    if c == 27:
        break


#cv.imshow('input image', src)

cv.waitKey(0)
cv.destroyAllWindows()

