import cv2 as cv
import numpy as np 

img=cv.imread("pics/park.jpg")
cv.imshow("park",img)

b,g,r = cv.split(img)

cv.imshow("blue",b)
cv.imshow("green",g)
cv.imshow("red",r)

merged = cv.merge([r,g,b])
cv.imshow("merged",merged)

blank = np.zeros(img.shape[:2],dtype='uint8')


blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
print(blue.shape)
cv.waitKey(0)