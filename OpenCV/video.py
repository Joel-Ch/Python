import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)

def color_quantization(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, label, center = cv.kmeans(
        data, k, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

while True:
    ret, frame = vid.read()
    cv.flip(frame, 1, frame)
    cv.imshow('frame', frame)
    frame = color_quantization(frame, 20)
    cv.imshow('frame2', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
vid.release()
cv.destroyAllWindows()