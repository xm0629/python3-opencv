import numpy as np
import cv2 as cv

'''
霍夫圆检测原理

x = a + Rcos(theta)
y = b + Rcos(theta)
Hought[theta][a][b] ++ 

霍夫圆变换原理, 
从平面坐标到极坐标转换三个参数 C(x0,y0,r) 其中 x0, y0 是圆心
假设平面坐标的任意一个圆上的点, 转换到极坐标中
C(x0,y0,r) 处有最大值, 霍夫变换正是利用这个原理, 实现圆的检测

现实的考量

因为 霍夫圆检测对噪声比较敏感, 所以首先要对图像做中值滤波

基于效率考虑, Opencv 中实现的霍夫变换圆检测是基于图像梯度的实现, 分为两步
1. 检测边缘, 发现可能的圆
2. 基于第一步的基础上从候选圆心开始计算最佳半径大小.

'''


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow('circles demo', image)


print('----------Hello Python----------')
src = cv.imread('./figure/coins.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()









