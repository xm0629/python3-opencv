import cv2 as cv
import numpy as np


'''
模板匹配:
1. 模板匹配就是在整个图像区域发现与给定子图象匹配的小块区域,
2. 模板匹配首先需要一个模板图像 T (给定的子图)
3. 需要一个待检测的图像-源图象 S
4. 工作方法, 在待检测图像上, 从左到右, 从上向下计算模板图像与重叠图像的匹配度, 匹配程度越大, 两者相同的可能性越大. 
模板匹配原理
Opencv 相关方法的使用
模板匹配的算法介绍
'''


def template_demo():
    tp1 = cv.imread('./figure/girls.jpg')
    tp2 = cv.imread('./figure/girls.jpg')
    cv.imshow('temapate image', tp1)
    cv.imshow('target image', tp2)
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th , tw = tp1.shape[:2]
    for md in methods:
        print(md)
        results = cv.matchTemplate(tp2, tp1, md)
        min_val, max_val , min_loc, max_loc = cv.minMaxLoc(results)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc

        br = (tl[0] + tw, tl[1] + th)
        cv.rectangle(tp2, tl, br, (0, 0, 255), 2)
        #cv.imshow('match-'+np.str(md), tp2)
        cv.imshow('match-' + np.str(md), results)


print('----------Hello Python----------')
src = cv.imread('./figure/girls.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

template_demo()
cv.waitKey(0)
cv.destroyAllWindows()
