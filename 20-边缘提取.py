import cv2 as cv

'''
边缘提取

Canny 算法介绍:
Canny 是边缘提取算法, 在1986 年提出的, 是一个很好用的边缘检测器, 很常用也很实用的图像处理方法.
步骤分为 5 步.
1. 高斯模糊 - GaussianBlur
2. 灰度转化 - cvtColor
3. 计算梯度 - Sobel/Scharr
4. 非最大信号抑制 #TODO不了解
5. 高低阈值输出二值图像
OpenCV 中的演示
'''

'''
\theta = \arctant{Gy}/{Gx} 求出一个角度, 
其中黄色区域的取值范围 0-22.5 与 157.5-180
绿色区域的取值范围 22.5-67.5
蓝色区域的取值范围 67.5-113.5
红色区域的取值范围 112.5-157.5

高低阈值连接
T1, T2 为阈值, 凡是高于 T2 的都保留, 凡是小于 T1 的都丢去, 从高于 T2 的像素出发, 凡是大于 T1 而且相互连接的都保留, 最终得到一个输出的二值图像

推荐的高低阈值比为 T2:T1 = 3:1/2:1 其中　T2 为高阈值, T1 为低阈值.
'''

def edge_demo(image):
    blur = cv.GaussianBlur(image, (3, 3), 0)#降低噪声
    gray = cv.cvtColor(blur, cv.COLOR_BGR2GRAY)
    gradx = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    grady = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(gradx, grady, 50, 150) # 高低阈值的取值
    cv.imshow('Canny image', edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow('Color Edge', dst)


print('----------Hello Python----------')
src = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()

