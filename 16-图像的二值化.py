'''
二值图像
图像二值化的方法

全局阈值
局部阈值
通过直方图可以直观的观察的二值化()

OPencv 中图像二值化方法
OTSU 
Triangle
自动化与手动
自适应阈值
Opencv 相关API的使用
'''


import cv2 as cv
import numpy as np


def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('threshold value %s' % (ret))
    cv.imshow('binary', binary)


def local_treshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    binary = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10)
    cv.imshow('binary', binary)


def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w*h])
    mean = m.sum()/(w*h)
    print('mean:', mean)
    ret, binary = cv.threshold(gray, mean, 255, cv.THRESH_BINARY)
    cv.imshow('binary', binary)


print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
custom_threshold(src)
cv.waitKey(0)
cv.destroyAllWindows()
