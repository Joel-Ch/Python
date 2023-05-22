import cv2 as cv
import numpy as np

def edges(val):
    imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', imgGray)
    imgBlur = cv.GaussianBlur(imgGray, (3,3), 0) 
    imgEdges = cv.Canny(imgBlur, val, val*2)
    cv.imshow('Edges', imgEdges)
    contours, hierarchy = cv.findContours(imgEdges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contourImg = np.zeros((imgEdges.shape[0], imgEdges.shape[1], 3), dtype=np.uint8)
    cv.drawContours(contourImg, contours, -1 ,(0,255,0), 2)

    maxContour = max(contours, key=cv.contourArea)
    x,y,w,h = cv.boundingRect(maxContour)
    cv.rectangle(contourImg,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv.imshow('Contours', contourImg)

image = cv.imread('adam.jpg')

imgWindow = 'Image'
cv.namedWindow(imgWindow)
cv.imshow(imgWindow, image)
thresh = 100
cv.createTrackbar('Canny Thresh:', imgWindow, thresh, 255, edges)
edges(thresh)

cv.waitKey(0)