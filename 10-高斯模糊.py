import cv2 as cv
import numpy as np

'''
高斯模糊: 高斯概率密度的分布,　使用高斯的函数需要已知的参数(sigma,x) 
操作:　常见模糊的计算方法.
高斯核:　行乘除, 列乘除 
卷积核: 加速的操作.

高斯模糊对高斯噪声有抑制作用
'''


def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    return pv


def gaussian_noise(image):
    h, w,c = image.shape
    for row in range(h):
        for col in range(w):
            for c in range(c):
                s = np.random.normal(0, 20, 3)
                b = image[row, col, 0]# Blue
                g = image[row, col, 1]# Green
                r = image[row, col, 2]# Red
                image[row, col, 0] = clamp(b + s[0])
                image[row, col, 1] = clamp(g + s[1])
                image[row, col, 2] = clamp(r + s[2])
    cv.imshow('noise image', image)


print('----------Hello Python----------')
src = cv.imread('./figure/girls.jpg')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print('time: %s ms' % (time*1000))

dst = cv.GaussianBlur(src, (5, 5), 15)
cv.imshow('Gauss image', dst)

cv.waitKey(0)
cv.destroyAllWindows()
