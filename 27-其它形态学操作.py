import numpy as np
import cv2 as cv


'''
其它形态学操作

1. 顶帽
顶帽是原图和开操作之间的差值图像
　
2. 黑帽

黑帽是闭操作和原图之间的差值
3. 形态学梯度
基本梯度
基本梯度是用膨胀后的图像减去腐蚀后的图像得到的差值图像,　称为梯度图像也是　opencv 中支持的计算形态学的梯度方法, 而此方法得到梯度有被称为基本梯度

内部梯度
是用原图像减去腐蚀后的图像得到的差值图像, 称为图像内部的梯度

外部梯度

图像膨胀后的图像减去原来图像得到的差值图图像, 称为图像的外部梯度.

代码层面的知识
'''


def top_bat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_TOPHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv.add(dst, cimage)
    cv.imshow('top hat image', dst)


def black_bat_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_BLACKHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv.add(dst, cimage)
    cv.imshow('black hat image', dst)


def hat_binary_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(binary, cv.MORPH_BLACKHAT, kernel)
    cimage = np.array(gray.shape, np.uint8)
    cimage = 100
    dst = cv.add(dst, cimage)
    cv.imshow('top hat image', dst)


def Jb_gradient(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dst = cv.morphologyEx(gray, cv.MORPH_GRADIENT, kernel)
    cv.imshow('black hat image', dst)


def outin_gradient(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    dm = cv.dilate(image, kernel)
    cm = cv.erode(image, kernel)
    dst1 = cv.subtract(image, cm)#in
    dst2 = cv.subtract(dm, image)#out

    cv.imshow('in gradient', dst1)
    cv.imshow('out gradient', dst2)


print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

outin_gradient(src)

#black_bat_demo(src)
#top_bat_demo(src)
#hat_binary_demo(src)

# Jb_gradient(src)

cv.waitKey(0)
cv.destroyAllWindows()


