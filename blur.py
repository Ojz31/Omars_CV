import cv2 as cv

img = cv.imread("pics/cats.jpg")
cv.imshow("cats",img)

#average 
average = cv.blur(img,(5,5))
cv.imshow("average",average)

#gauss
gauss = cv.GaussianBlur(img,(5,5),0)
cv.imshow("gauss",gauss)

#median 
median = cv.medianBlur(img,5)
cv.imshow("median",median)

#bilertal
bil = cv.bilateralFilter(img,15,30,25)
cv.imshow("bil",bil)

#erode
erode = cv.Canny(bil,300,350)
cv.imshow("erode",erode)

cv.waitKey(0)