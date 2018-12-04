import cv2 as cv
import numpy as np


'''
图像金字塔：
图像金字塔原理
reduce = 高斯模糊 + 降采样
高斯模模糊 + 偶数行采样，偶数列采样， 可以一层一层向上递归.不能跳层
expend = 扩大 + 卷积、

图像的深采样，

高斯的金字塔与拉普拉斯金字塔
l1 = g1 -expend(g2)

可以从高斯金字塔得到拉普拉斯金字塔


代码层面的知识
PyrDown: 降采样
Pyrup: 还原
高斯金字塔与拉普拉斯金字塔
'''


def pyramid_demo(image):
    level = 3#3层金字塔
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow('pyramid_dem' + str(i), dst)
        temp = dst.copy()
    return pyramid_images


def laplace_demo(image):
    pyramid_image = pyramid_demo(image)
    level = len(pyramid_image)
    for i in range(level-1, -1, -1):
        # 最后一层特殊处理
        if (i-1) < 0:
            expand = cv.pyrUp(pyramid_image[i], dstsize=image.shape[:2])
            laplace = cv.subtract(image, expand)
            cv.imshow('laplace demo' + str(i), laplace)
        else:
            expand = cv.pyrUp(pyramid_image[i], dstsize=pyramid_image[i-1].shape[:2])
            laplace = cv.subtract(pyramid_image[i-1],  expand)
            cv.imshow('laplace demo' + str(i), laplace)

# 这里有一个经常用得到的坑, 必须要把原图变为整数2的n次方.

print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

#pyramid_demo(src)
laplace_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

