import cv2 as cv
import numpy as np

image = cv.imread('adam.jpg')

cv.imshow("Image", image)

sobel = cv.Sobel(image, cv.CV_64F, 1, 1)
canny = cv.Canny(image, 100, 200)

cv.imshow("Sobel", sobel)
cv.imshow("Canny", canny)


cv.waitKey(0)