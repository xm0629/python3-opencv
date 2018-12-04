

'''
超大图像二值化方法
分块
全阈值 vs 局部阈值
'''

import cv2 as cv
import numpy as np


def big_image_demo(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            #ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY|cv.THRESH_OTSU) # 全局阈值
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20) # 自适应阈值
            gray[row:row+ch, col:col+cw, ] = dst
            print(np.std(dst), np.mean(dst))

    cv.imwrite('./figure/result_binary.png', gray)


def Big_image_demo(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            print(np.std(dst), np.mean(dst))
            dev = np.std(roi)
            if dev < 15:
                gray[row:row + ch, col:col + cw, ] = 255
            else:
                # 全局阈值过滤超大图像的而二值化
                ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                #dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 20)
                gray[row:row + ch, col:col + cw, ] = dst
    cv.imwrite('./figure/result_binary.png', gray)



print('----------Hello Python----------')
src = cv.imread('./figure/bigimage.jpeg')
#cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
#cv.imshow('input image', src)
big_image_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
