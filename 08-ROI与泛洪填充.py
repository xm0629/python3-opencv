import numpy as np
import cv2 as cv

'''
ROI, 对图像上感兴趣的区域, Region of interest, 如何获取 ROI 通过 numpy, 这个区域怎么确定

泛洪填充, 开始点的选择,
泛洪填充, 如何填充一个对象内部区域, 
FLOODFILL_FIXED_RANGE 改变图象, 泛洪填充
FLOODFILL_MASK_ONLY, 不改变图像, 只填充遮罩层本身, 忽略新的颜色值参数

'''


# 两种填充模式

def fill_color_demo(image):
    copyIMG = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8) # 输入参数必须是这样
    cv.floodFill(copyIMG, mask, (30, 30), (0, 255, 255), (100, 100, 100,), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow('fill_color_demo', copyIMG)


def fill_binary_demo():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 255
    cv.imshow('fill_binary_demo', image)
    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,255,255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow('fill binary demo', image)





print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

fill_color_demo(src)

fill_binary_demo()
'''

face = src[50:250, 100:300]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

src[50:250, 100:300] = backface
cv.imshow('gray', src)
'''

cv.waitKey(0)
cv.destroyAllWindows()

