import numpy as np
import cv2 as cv

'''
弧长与面积
轮廓发现
计算每个轮廓的弧长与面积, 像素单位
多边形拟合
获取轮廓的多边形拟合结果
approxPolyDP
contour
epsilon 越小越折线越逼近真实形状, 
close 是否为闭合区域

原点矩 
中心矩
图像的重心坐标

代码层面的知识
'''


def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print('threshold value: %s' % (ret))
    cv.imshow('binary image', binary)

    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    outImage, contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h)/max(w, h)
        print('rectangle rate: %s' % (rate))
        mm = cv.moments(contour)# 几何矩
        print(type(mm))
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(dst, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        #cv.rectangle(dst, (x, y), (x+w, y+h), (0, 0, 255), 2)
        print('contour area %s' %(area))
        approxCure = cv.approxPolyDP(contour, 4, True)
        print(approxCure.shape)
        if approxCure.shape[0] > 10:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCure.shape[0] == 4:
            cv.drawContours(dst, contours, i, (0, 0, 255), 2)
            if approxCure.shape[0] == 3:
                cv.drawContours(dst, contours, i, (255, 0, 0), 2)
    cv.imshow('measure-contours', dst)


print('----------Hello Python----------')
src = cv.imread('./figure/pic5.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

measure_object(src)

cv.waitKey(0)
cv.destroyAllWindows()


