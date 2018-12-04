import numpy as np
import cv2 as cv

'''
开闭操作
闭操作
代码层面知识
开操作

图形形态学的重要操作之一, 基于膨胀与腐蚀操作组合形成的.
主要是应用在二值图像分析中, 灰度图像亦可
开操作=腐蚀+膨胀, 输入图像 + 结构元素.

闭操作
图像形态学的重要操作之一, 基于膨胀与腐蚀操作组合形成的
主要是应用在二值图形分析中,　灰度图像亦可
闭操作 = 膨胀加腐蚀, 输入图像　+ 结构元素

结构元素的选择, 和大小的调整

'''

def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow('binary1 demo', binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 1))
    binary = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel)
    cv.imshow('opne results', binary)

def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary2 demo', binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 15))
    binary = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    cv.imshow('close results', binary)


print('----------Hello Python----------')
src = cv.imread('./figure/morph01.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

open_demo(src)

#close_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

