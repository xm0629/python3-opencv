import numpy as np
import cv2 as cv


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow('add_demo', dst)


def subtract_demo(m1, m2):
    dsb = cv.subtract(m1, m2)
    cv.imshow('subtract_demo', dsb)


def divide_demo(m1, m2):
    dsv = cv.divide(m1, m2)
    cv.imshow('divide_demo', dsv)


def multiply(m1, m2):
    dsm = cv.multiply(m1, m2)
    cv.imshow('divide_demo', dsm)


def others(m1, m2):
    M1 = cv.mean(m1)
    M2 = cv.mean(m2)


def others2(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)

    h, w = m1.shape[:2]
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

    img = np.zeros([h,w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m) # 通过均值和方差比较, 方差小于某个阈值,图像是无效的
    print(dev)


def logic_demo(m1, m2):
    dst = cv.bitwise_and(m1, m2)
    cv.imshow('logic_demo', dst)


def logic_demo1(m1, m2):
    dst = cv.bitwise_or(m1, m2)
    cv.imshow('logic_demo1', dst)


def logic_demo2(m1, m2):
    dst = cv.bitwise_not(m1, m2)
    cv.imshow('logic_demo2', dst)


def contrast_brightness_demo(image, c, b):
    '''
    :param image: 图片
    :param c: 对比度
    :param b: 亮度
    :return: 调整对比度和亮度的图片
    '''
    h, w, ch = image.shape
    blank = np.zeros([h, w, ch], image.dtype)
    dst = cv.addWeighted(image, c, blank, 1-c, b)
    cv.imshow('contrast-b-demo', dst)


print('------------Hello Python--------------')
src1 = cv.imread('./figure/LinuxLogo.jpg')
src2 = cv.imread('./figure/WindowsLogo.jpg')

print(src1.shape)
print(src2.shape)

cv.namedWindow('input1 image', cv.WND_PROP_AUTOSIZE)
cv.imshow('input1 image', src1)
cv.imshow('imput2 image', src2)

src = cv.imread('./figure/lena1.png')
cv.imshow('input image', src)
contrast_brightness_demo(src, 1.2, 20) #(图片,对比度,亮度)


# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply(src1, src2)
# others(src1, src2)
# others2(src1, src2)

# logic_demo(src1, src2)
# logic_demo1(src1, src2)
# logic_demo2(src1, src2)

cv.waitKey(0)
cv.destroyAllWindows()