# Importing Libraries
import cv2 as cv
import numpy as np

# Importing Original Image
img = cv.imread('1.jpg')
# Showing Original Image
cv.imshow('Original Image',img)  


lower_range = np.array([0,0,0]) 
upper_range = np.array([200,100,255])  
mask = cv.inRange(img,lower_range,upper_range) 
result = cv.bitwise_and(img,img,mask = mask)  
cv.imshow('Color Detected Image',result) 


cv.waitKey(0)

#closing the windows
cv.destroyWindow('Color Detected Image')
cv.destroyWindow('Original Image')
