# Importing Libraries
import cv2 as cv
import numpy as np

#getting values of the range
print("Range example: ([220,120,255]) here these numbers are a,b,c respectively")
a=int(input("Enter 'x' for the range: "))
b=int(input("Enter 'x' for the range: "))
c=int(input("Enter 'y' for the range: "))

# Importing Original Image
img = cv.imread('1.jpg')
# Showing Original Image
cv.imshow('Original Image',img)  



lower_range = np.array([0,0,0]) 
upper_range = np.array([a,b,c])  
mask = cv.inRange(img,lower_range,upper_range) 
result = cv.bitwise_and(img,img,mask = mask)  
cv.imshow('Color Detected Image',result) 


cv.waitKey(0)

#closing the windows
cv.destroyWindow('Color Detected Image')
cv.destroyWindow('Original Image')
