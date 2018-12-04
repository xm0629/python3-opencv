import cv2 as cv
import numpy as np

'''
边缘保留滤波:(EPF)通常叫做卷积, 有相关的API, 怎么使用 API, 理解高斯双边模糊的原理, 边缘方差差异很大, 实现的方法很多, OPENCV 给出以下两个 API.

高斯双边
均值迁移
操作
'''


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)#参数
    cv.imshow('bi demo', dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)#参数
    cv.imshow('shift demo', dst)


print('----------Hello Python----------')
src = cv.imread('./figure/example.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
bi_demo(src)
shift_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
