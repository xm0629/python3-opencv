import cv2 as cv
import numpy as np

'''
图像梯度

一阶导数与Soble 算子
图像边缘:
比如头发和脸边缘的变化, 像素的差异, 使用一个和卷积一样的掩模算子, 类似卷积, 在图像上移动, 在边缘上的值最大, 水平加垂直的总的梯度的大小.

二阶导数与拉普拉斯算子

二阶导数
在二阶导数的时候, 最大变化处的值为零即边缘是零值, 通过二阶导数计算, 依据此理论我们可以计算图像二阶导数, 提取边缘值.

laplace(f) = \frac{\pattial^2 f}{\partial x^2} + \frac{\pattial^2 f}{\partial y^2} 


代码层面知识
Soble 算子
拉普拉斯算子
OpenCV API 的应用
'''

def sobel_demo(image):
    '''
    Scharr 算子是 Sobel 增强的算子, 更能得到增强的边缘.
    '''
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow('gradient x', gradx)
    cv.imshow('gradient y', grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow('gradident xy', gradxy)


def laplace_atu_demo(image):
    kernel = np.array([[0, 1, 0], [1, -8, 1], [0, 1, 0]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    laplace_atu = cv.convertScaleAbs(dst)
    cv.imshow('laplace-atu', laplace_atu)


def laplace_demo(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    laplace = cv.convertScaleAbs(dst)
    cv.imshow('laplace image', laplace)


print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

laplace_atu_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()



