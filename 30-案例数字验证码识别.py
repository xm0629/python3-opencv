import numpy as np
import cv2 as cv
from PIL import Image
import pytesseract as tess


'''
数字验证码识别
主要知识点
1. 预处理- 去除干扰线和点
2. 不同的结构元素中选择
3. Image 与 NumPy　array 相互转化
4. 识别与输出  
'''

def recognize_text():
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    kenerl = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    bin1 = cv.morphologyEx(binary, cv.MORPH_OPEN, kenerl)

    kenerl = cv.getStructuringElement(cv.MORPH_RECT, (2, 1))
    openout = cv.morphologyEx(bin1, cv.MORPH_OPEN, kenerl)
    cv.imshow('binary image', openout)

    cv.bitwise_not(openout, openout)
    textImage = Image.fromarray(openout)
    text = tess.image_to_string(textImage)
    print('识别结果: %s' % text)



print('----------Hello Python----------')
src = cv.imread('./figure/5374.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)
cv.imshow('input image', src)

recognize_text()

cv.waitKey(0)
cv.destroyAllWindows()
