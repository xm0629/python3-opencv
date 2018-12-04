import numpy as np
import cv2 as cv

'''
直线检测, 

霍夫直线变换介绍
相关 API 代码演示

Hought Line  Transform 用来做直线检测
前提条件- 边缘检测已经完成
平面空间到极坐标空间转换

x = \rhocos\theta
y = \rhosin\theta

\rho^2 = x^2 + y^2,
\tan\theta = y/x (x\neq 0)
'''


def line_detection(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edge, 1, np.pi/180, 200)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow('image-lines', image)


def line_delect_prossible_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edge, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0,0, 255), 2)
    cv.imshow('line_delect_prossible_demo', image)



print('----------Hello Python----------')
src = cv.imread('./figure/morph01.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
line_delect_prossible_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()


