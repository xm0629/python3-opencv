# 模糊操作
'''
均值模糊
中值模糊
自定义模糊
实际是数学上的卷积的操作
1. 基于离散卷积
2. 定义好每个卷积核
3. 不同卷积核得到不同的卷积效果
4. 模糊是卷积的一种表现

卷积原理
卷积核的大小都要是奇数, 卷积边缘的值没有处理

'''

import cv2 as cv
import numpy as np


def blur_demo(image):
    dst = cv.blur(image, (15, 1))
    cv.imshow('input image', dst)


def median_blur_demo(image): # 去噪
    dst = cv.medianBlur(image, )
    cv.imshow('input1 image', dst)



def custom_blur_demo(image): # 去噪
    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow('custom image', dst)


print('----------Hello Python----------')
src = cv.imread('./figure/lenanoise1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)


#blur_demo(src)
#median_blur_demo(src)
custom_blur_demo(src)


cv.waitKey(0)
cv.destroyAllWindows()
