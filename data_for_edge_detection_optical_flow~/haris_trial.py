import numpy as np
import cv2 

cap = cv2.VideoCapture('Ati.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    #cv2.imshow('dst',dst)
    dst = cv2.dilate(dst,None)
    frame[dst>0.01*dst.max()]=[0,0,255]
    #cv2.imshow('dst',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






