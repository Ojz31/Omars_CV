import cv2 as cv

img = cv.imread("pics/cats.jpg")
cv.imshow("cat",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray,120,256,cv.THRESH_BINARY_INV)

cv.imshow("simple threshhold", thresh)


#advaptive

advaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,10)
cv.imshow("adaptive",advaptive)

cv.waitKey(0)