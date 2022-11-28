import numpy as np
import cv2 as cv
cap = cv.VideoCapture('ati_short.mp4')
while(1):
    ret,frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = np.float32(frame_grey)
    dst = cv.cornerHarris(gray,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv.imshow('dst',erfewf)
cap.release()
cv.destroyAllWindows()

