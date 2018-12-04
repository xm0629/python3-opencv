import cv2 as cv
import matplotlib.pyplot as plt


'''
直方图反向投影:

HSV 与 RGB 色彩空间
反向投影
'''


def back_project_demo():
    sample = cv.imread('./figure/sample-07.png')# 换图片
    target = cv.imread('./figure/07.jpg')
    roi_hsv = cv.cvtColor(sample, cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target, cv.COLOR_BGR2HSV)

    # show image
    cv.imshow('sample image', sample)
    cv.imshow('target image', target)
    roiHist = cv.calcHist([roi_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv.normalize(roiHist, roiHist, 0, 255, cv.NORM_MINMAX)
    dst = cv.calcBackProject(target_hsv, [0, 1], roiHist, [0, 180, 0, 256], 1)
    cv.imshow('BackProject demo', dst)


def hist2d_demo(image):
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image], [0, 1], None, [180, 256], [0, 180, 0, 256])

    #cv.imshow('hist2d demo', hist)

    plt.imshow(hist, interpolation='nearest')
    plt.title('2D Histogram')
    plt.show()


print('----------Hello Python----------')
src = cv.imread('./figure/girls.jpg')
# cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
# cv.imshow('input image', src)

back_project_demo()

cv.waitKey(0)
cv.destroyAllWindows()

