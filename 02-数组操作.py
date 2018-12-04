import cv2 as cv
import numpy as np


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print('height', height)
    print('width', width)
    print('channels', channels)

    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow('pixels_demo', image)


def creat_image_demo():
    '''
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 2] = np.ones([400, 400])*255
    cv.imshow('new image', img)
    '''

    '''
    img = np.zeros([400, 400, 1], np.uint8)
    img[:, :, 0] = np.ones([400, 400]) * 127
    cv.imshow('new single image', img)
    cv.imwrite('./figure/xm_1.png')
    
    '''

    m1 = np.ones([3, 3], np.float32)
    m1.fill(122.388)
    print(m1)
    m5 = m1.reshape([1, 9])
    print(m5)

    m2 = np.ones([3, 3], np.uint8)
    m2.fill(122.388)
    print(m2)

    m3 = np.ones([3, 3], np.uint32)
    m3.fill(122.388)
    print(m3)

    m4 = np.ones([3, 3], np.uint8)
    m4.fill(122.388)
    print(m4)


print('----------- Hello Python-----------')
src = cv.imread('./figure/LinuxLogo.jpg')#Blue Green Red (BGR)
cv.namedWindow('Linux image', cv.WND_PROP_AUTOSIZE)
cv.imshow('Linux image', src)


t1 = cv.getTickCount()
creat_image_demo()
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("Time: %s ms" % (time*1000))


cv.waitKey(0)
cv.destroyAllWindows()
