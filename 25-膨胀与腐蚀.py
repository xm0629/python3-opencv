import numpy as np
import cv2 as cv

'''
膨胀与腐蚀
膨胀 结构元素覆盖下的最大值, 最大滤波

膨胀的作用

或

1. 对象大小增加一个像素(3,3)
2. 平滑对象边缘
3. 减少或者填充对象之间的距离


腐蚀
交 最小值替换中心像素

相关的 API 代码实现

图形形态学
是图像处理科学的一个单独分支学科
灰度与二值图像处理中重要手段
是由数学的集合论等相关理论发展起来的

'''


def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 1))
    dst = cv.erode(binary, kernel)
    cv.imshow('erode_demo', dst)


def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow('erode_demo', dst)


print('----------Hello Python----------')
src = cv.imread('./figure/LinuxLogo.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
dilate_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
