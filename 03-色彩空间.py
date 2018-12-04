import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('height', height)
    print('width', width)
    print('channels', channels)

    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow('pixels_demo', image)


def inverse_demo(image):
    #取反的高效性
    dst = cv.bitwise_not(image)
    cv.imshow('inverse demo', dst)


print('----------- Hello Python-----------')
src = cv.imread('./figure/LinuxLogo.jpg')  # Blue Green Red (BGR)
cv.namedWindow('Linux image', cv.WND_PROP_AUTOSIZE)
cv.imshow('Linux image', src)

t1 = cv.getTickCount()
inverse_demo(src)
t2 = cv.getTickCount()
time = (t2 - t1) / cv.getTickFrequency()
print("Time: %s ms" % (time * 1000))

cv.waitKey(0)
cv.destroyAllWindows()
