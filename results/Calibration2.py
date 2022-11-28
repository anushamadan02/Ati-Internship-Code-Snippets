import numpy as np
import cv2 as cv
import glob
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)#max no of iterations, accuracy #termination Criteria
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*6,3), np.float32)#world object points
objp[:,:2] = np.mgrid[0:6,0:6].T.reshape(-1,2) #(no of rows, no of elements)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space, if the pic is suitable
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.png')
count=0
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners                             #image, pattern size
    ret, corners = cv.findChessboardCorners(gray,(6,6), None)#7 rows and 6 columns #internal points only are found #ret is true or false if points can be found in an image
    #cv.imshow('img', ret)#small black and white pixels
    #print(corners) 11 pictures with 42 point coordinates
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria) #(image, corners, win, zero_zone, criteria)
        #corners2 each of the 11 images chosen had 42 coordinate points of the corners
        imgpoints.append(corners2)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (6,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)
print(gray.shape)
print(gray.shape[::-1])
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
print(mtx)#gray.shape is the shape of the image #outputs return val, K, k,R,T
img = cv.imread('image-10450.png')#here we are applying the calliberation to this particular image.
print(img.shape)
print(img.shape[:2])
h,  w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))#undistortion of a matrix, 1 is the alpha #if alpha=1 retains all image pixels but there will be black to make up for warped image correction
# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)#corrections
cv.waitKey(500)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w] # Corrections applied 
cv.imwrite('calibresult.png', dst)
cv.waitKey(500)
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)#object point to image point we are transforming#actual
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
    mean_error += error
print( "total error: {}".format(mean_error/len(objpoints)) )
cv.destroyAllWindows()

