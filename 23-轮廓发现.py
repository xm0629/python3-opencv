import cv2 as cv
'''
轮廓发现: 是基于图像边缘提取的基础寻找对象轮廓的方法, 所以边缘提取的阈值选定会影响最终的轮廓发现结果.

API 介绍
1. findContours 发现轮廓
2. drawContours 绘制轮廓

如何利用梯度来避免阈值烦恼
'''


def edge_demo(image):
    blur = cv.GaussianBlur(image, (3, 3), 0)#降低噪声
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    edge_output = cv.Canny(gray, 50, 150) # 高低阈值的取值
    cv.imshow('Canny image', edge_output)
    return edge_output


def contours_demo(image):
    '''
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary image', binary)
    '''

    binary = edge_demo(image) # 第二种方法的结合
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 255, 255), -1) # -1 填充颜色, 2 不填充颜色, 具体参数还需查
        print(i)
    cv.imshow('contours image', image)


print('----------Hello Python----------')
src = cv.imread('./figure/coins.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

