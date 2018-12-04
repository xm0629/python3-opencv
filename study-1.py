import numpy as np
import cv2 as cv
import os


randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv.imwrite('./figure/RandomGray.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv.imwrite('./figure/RandomBGR.png',bgrImage)

img = cv.imread('./figure/lena1.png')
cv.namedWindow('input image', cv.WINDOW_AUTOSIZE)

img[20, 20] = [255, 255, 255]
print(img)
cv.imshow('input image', img)
cv.waitKey(0)
cv.destroyAllWindows()
