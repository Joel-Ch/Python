import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

def edges(image):
    imgGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # cv.imshow('Gray', imgGray)
    imgBlur = cv.GaussianBlur(imgGray, (3,3), 0)
    imgEdges = cv.Canny(imgBlur, 50, 150)
    # cv.imshow('Edges', imgEdges)
    contours, hierarchy = cv.findContours(imgEdges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contourImg = np.zeros((imgEdges.shape[0], imgEdges.shape[1], 3), dtype=np.uint8)
    for i in range (len(contours)):
        j = np.interp(i, [0, len(contours)], [0, 255])
        cv.drawContours(contourImg, contours, i ,(abs(255-j),0,j), 2)

    maxContour = max(contours, key=cv.contourArea)
    x,y,w,h = cv.boundingRect(maxContour)
    cv.rectangle(contourImg,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv.imshow('Contours', contourImg)
    
    return contours

def dilateErode(frame):
    # find eges
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (3,3), 0)
    imgEdges = cv.Canny(imgBlur, 50, 150)
    cv.imshow('Edges', imgEdges)
    
    # dilate
    elementDilate = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    cv.dilate(imgEdges, elementDilate, imgEdges)
    cv.imshow('dilated', imgEdges)

    # floodfill
    floodFilled = imgEdges.copy()
 
    h, w = floodFilled.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    cv.floodFill(imgEdges, mask, (round(w/2),round(h/2)), (0,0,0))
    cv.imshow('floodfilled', floodFilled)

    # erode
    erosionElement = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    cv.erode(floodFilled, erosionElement, floodFilled)
    
    cv.imshow('eroded', floodFilled)

    # find contours
    contours = cv.findContours(floodFilled, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # cv.drawContours(frame, contours, -1, (0,0,255))
    
    # # find largest contour
    # maxContour = max(contours, key=cv.contourArea)
    # cv.polylines(frame, maxContour, True, (0,255,0))

    # cv.imshow('Contours', frame)
    # return maxContour

while True:
    ret, frame = vid.read()
    cv.flip(frame, 1, frame)
    cv.imshow('frame', frame)
    # contours = edges(frame)
    singleContour = dilateErode(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()