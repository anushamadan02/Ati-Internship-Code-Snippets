import numpy as np
import cv2

cap = cv2.VideoCapture('Ati.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,150,210)
    edges1=cv2.Canny(frame,100,200)
    edges2=cv2.Canny(frame,80,150)
    
    cv2.imshow('Sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    '''
    cv2.imshow('laplacian',laplacian)
    
    cv2.imshow('original',frame)
    cv2.imshow('canny150-210',edges)
    cv2.imshow('canny100-200',edges1)
    cv2.imshow('canny80-150',edges2)
    
    print(sobelx)
    print(sobely)
    print(laplacian)
    '''

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
