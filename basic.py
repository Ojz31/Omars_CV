import cv2 as cv

img = cv.imread("pics/park.jpg")

# cv.imshow("park",img)

# #gray scale

# grayScale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",grayScale)

# #blur 
blur = cv.blur(img,(7,7))
#cv.imshow("blur",blur)

# blurr = cv.blur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blur with border",blurr)


#edge detection 
edge = cv.Canny(blur,125,175)
cv.imshow("canny",edge)

edgee = cv.Canny(blur,175,200)
cv.imshow("cannyyy",edgee)

#dialate
dialte = cv.dilate(edge,(7,7),iterations=3)
cv.imshow("dialte",dialte)

#erode
erdode = cv.erode(dialte,(7,7),iterations=3)
cv.imshow("erode",erdode)

#hello

cv.waitKey(0)