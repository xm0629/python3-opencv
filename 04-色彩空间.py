import numpy as np
import cv2 as cv



print('----------- Hello Python-----------')
src = cv.imread('./figure/LinuxLogo.jpg')#Blue Green Red (BGR)
cv.namedWindow('Linux image', cv.WND_PROP_AUTOSIZE)
cv.imshow('Linux image', src)

cv.waitKey(0)
cv.destroyAllWindows()
