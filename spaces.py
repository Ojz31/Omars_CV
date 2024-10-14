import cv2 as cv

img = cv.imread("pics/park.jpg")

cv.imshow("park",img)

#BGR to gray

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#bgr to hsv
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#bgr to lab 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#lab to bgr
bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("bgr",bgr)

cv.waitKey(0)