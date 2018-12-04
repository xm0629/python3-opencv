import numpy as np
import cv2 as cv

'''
分水岭算法

距离变换
分水岭变换介绍
opencv 分水岭算法演示
'''


def watershed_dem(src):
    print(src.shape)
    # 去噪
    blurred = cv.pyrMeanShiftFiltering(src, 10, 100)

    # gray image
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary image', binary)

    # 形态学的操作

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    cv.imshow('mor-ope', sure_bg)

    # 对　mb 距离变换
    dsit = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dsit, 0, 1.0, cv.NORM_MINMAX)
    cv.imshow('distance-t', dist_output*50)

    ret, surface = cv.threshold(dsit, dsit.max()*0.6, 255, cv.THRESH_BINARY)
    cv.imshow('surface-binary', surface)

    # 转成8 位得到种子
    surface_fg = np.uint8(surface)

    unknown = cv.subtract(sure_bg, surface_fg)

    ret, markers = cv.connectedComponents(surface_fg)
    print(ret)
    
    # 完成分水岭变换
    markers = markers - 1
    markers[unknown == 255] = 0
    markers = cv.watershed(src, markers=markers)
    src[markers == -1] = [0, 0, 255]
    cv.imshow('result image', src)





print('----------Hello Python----------')
src = cv.imread('./figure/coins.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
watershed_dem(src)
cv.waitKey(0)
cv.destroyAllWindows()
