import numpy as np
import cv2 

cap = cv2.VideoCapture('Ati.mp4')
lk_params = dict( winSize  = (6,6),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
gray = np.float32(old_gray)
dst = cv2.cornerHarris(gray,2,3,0.04)
count=0
dst = cv2.dilate(dst,None)

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    count=count+1
    print(dst)
    if count==10:
        break
    #cv2.imshow('dst',dst)
    dst = cv2.dilate(dst,None)
    frame[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('dst',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    old_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()


