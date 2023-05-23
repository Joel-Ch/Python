import cv2 as cv
import numpy as np
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation


segmentor = SelfiSegmentation()

vid = cv.VideoCapture(0)

def removeBG(frame):
    #resize office to 640x480
    frame = cv.resize(frame, (640, 480))


    imgNoBg = segmentor.removeBG(frame, (0,0,0), threshold=0.50)

    # show both images
    cv.imshow('office',frame)
    cv.imshow('office no bg',imgNoBg)

while True:
    ret, frame = vid.read()
    cv.flip(frame, 1, frame)
    cv.imshow('frame', frame)

    removeBG(frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()