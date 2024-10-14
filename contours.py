import cv2 as cv
import numpy as np 

img = cv.imread("pics/cats.jpg")
cv.imshow("cats",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')

cv.imshow("black",blank)


blur = cv.blur(gray,(7,7))
cv.imshow("blur",blur)

canny = cv.Canny(blur,100,175)
cv.imshow("canny",canny)

contour, heicharies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} is the contours found')

cv.drawContours(blank,contour,-1,(0,255,0),2)
cv.imshow("contour",blank)

cv.waitKey(0)