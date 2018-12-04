import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


'''
图像直方图:
一维与多维
图像的像素值是 0-255 进行统计, 

'''


def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show('直方图')


def image_hist(image):
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


print('----------Hello Python----------')
src = cv.imread('./figure/girls.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

image_hist(src)

cv.waitKey(0)
cv.destroyAllWindows()
