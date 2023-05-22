import cv2 as cv
import numpy as np

backSub = cv.createBackgroundSubtractorKNN()
backSub2 = cv.createBackgroundSubtractorMOG2()


vid = cv.VideoCapture(0)


while True:
    ret, frame = vid.read()
    cv.flip(frame, 1, frame)
    cv.imshow('frame', frame)
    
    fgMask = backSub.apply(frame)
    fg2Mask = backSub2.apply(frame)
    
    frame = cv.bitwise_and(frame, frame, mask=fg2Mask)
    frame2 = cv.bitwise_and(frame, frame, mask=fgMask)
    cv.imshow('masked', frame)
    cv.imshow('masked2', frame2)
    
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()