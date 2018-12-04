import cv2 as cv
import numpy as np


'''
直方图应用, 调整图像的对比度, 常用的两个 API 接口


直方图的均衡轮廓
直方图比较
'''


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow('equalHist image', dst)

def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow('clahe image', dst)


def creat_RGB_hist(image):
    h, w, c = image.shape
    rgbhist = np.zeros([16*16*16, 1], np.float32)
    bsize = 256/16

    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b/bsize)*16*16 + np.int(g/bsize)*16 + np.int(r/bsize)
            rgbhist[np.int(index), 0] + 1
    return rgbhist


def hist_compare(image1, image2):
    hist1 = creat_RGB_hist(image1)
    hist2 = creat_RGB_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print('巴氏距离: %s, 相关性: %s, 卡方: %s' % (match1, match2, match3))


print('----------Hello Python----------')
src = cv.imread('./figure/girls.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

src1 = cv.imread('./figure/restlt.png')
src2 = cv.imread('./figure/lena1.png')
cv.imshow('input image1', src1)
cv.imshow('input image2', src2)
hist_compare(src1, src2)

cv.waitKey(0)
cv.destroyAllWindows()
