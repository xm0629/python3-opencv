import cv2 as cv
import numpy as np


def get_image2info(image):
    print(image.shape)
    print(image.size)
    print(image.dtype)
    pixel_data = np.array(image)
    print(pixel_data)


def get_video_demo():
    capture = cv.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        cv.flip(frame, 1)
        cv.imshow('video', frame)
        c = cv.waitKey(50)
        if c == 27:
            break
    # 保存视频


print('----------- Hello Python-----------')
image = cv.imread('./figure/LinuxLogo.jpg')
cv.namedWindow('Linux image', cv.WND_PROP_AUTOSIZE)

cv.imshow('Linux image', image)
get_image2info(image)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

cv.imwrite('./figure/xm_linux.png', gray)

#get_video_demo()


cv.waitKey(0)
cv.destroyAllWindows()


