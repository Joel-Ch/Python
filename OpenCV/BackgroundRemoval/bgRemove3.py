import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)


def bgremove(frame):
    # First Convert to Grayscale
    frameGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
    ret,baseline = cv.threshold(frameGray,127,255,cv.THRESH_TRUNC)
 
    ret,background = cv.threshold(baseline,126,255,cv.THRESH_BINARY)
 
    ret,foreground = cv.threshold(baseline,126,255,cv.THRESH_BINARY_INV)
 
    foreground = cv.bitwise_and(frame,frame, mask=foreground)  # Update foreground with bitwise_and to extract real foreground
 
    # Convert black and white back into 3 channel greyscale
    background = cv.cvtColor(background, cv.COLOR_GRAY2BGR)
 
    # Combine the background and foreground to obtain our final image
    finalimage = background+foreground
    return finalimage


def bgremove2(myimage):
    # BG Remover 3
    myimage_hsv = cv.cvtColor(myimage, cv.COLOR_BGR2HSV)
     
    #Take S and remove any value that is less than half
    s = myimage_hsv[:,:,1]
    s = np.where(s < 127, 0, 1) # Any value below 127 will be excluded
 
    # We increase the brightness of the image and then mod by 255
    v = (myimage_hsv[:,:,2] + 127) % 255
    v = np.where(v > 127, 1, 0)  # Any value above 127 will be part of our mask
 
    # Combine our two masks based on S and V into a single "Foreground"
    foreground = np.where(s+v > 0, 1, 0).astype(np.uint8)  #Casting back into 8bit integer
 
    background = np.where(foreground==0,255,0).astype(np.uint8) # Invert foreground to get background in uint8
    background = cv.cvtColor(background, cv.COLOR_GRAY2BGR)  # Convert background back into BGR space
    foreground=cv.bitwise_and(myimage,myimage,mask=foreground) # Apply our foreground map to original image
    finalimage = background+foreground # Combine foreground and background
 
    return finalimage

def bgremove3(myimage):
 
    # Blur to image to reduce noise
    myimage = cv.GaussianBlur(myimage,(5,5), 0)
 
    # We bin the pixels. Result will be a value 1..5
    bins=np.array([0,51,102,153,204,255])
    myimage[:,:,:] = np.digitize(myimage[:,:,:],bins,right=True)*51
 
    # Create single channel greyscale for thresholding
    myimage_grey = cv.cvtColor(myimage, cv.COLOR_BGR2GRAY)
 
    # Perform Otsu thresholding and extract the background.
    # We use Binary Threshold as we want to create an all white background
    ret,background = cv.threshold(myimage_grey,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
 
    # Convert black and white back into 3 channel greyscale
    background = cv.cvtColor(background, cv.COLOR_GRAY2BGR)
 
    # Perform Otsu thresholding and extract the foreground.
    # We use TOZERO_INV as we want to keep some details of the foregorund
    ret,foreground = cv.threshold(myimage_grey,0,255,cv.THRESH_TOZERO_INV+cv.THRESH_OTSU)  #Currently foreground is only a mask
    foreground = cv.bitwise_and(myimage,myimage, mask=foreground)  # Update foreground with bitwise_and to extract real foreground
 
    # Combine the background and foreground to obtain our final image
    finalimage = background+foreground
 
    return finalimage



while True:
    ret, frame = vid.read()
    cv.flip(frame, 1, frame)
    cv.imshow('frame', frame)
    
    noBg = bgremove(frame)
    noBg2 = bgremove2(frame)
    noBg3 = bgremove3(frame)
    
    cv.imshow('no bg', noBg)
    cv.imshow('no bg2', noBg2)
    cv.imshow('no bg3', noBg3)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()