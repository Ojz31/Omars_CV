import cv2 as cv
import numpy as np

img = cv.imread("pics/cats.jpg")
cv.imshow("cats",img)

blank = np.zeros(img.shape[:2],dtype="uint8")

masks = cv.rectangle(blank,(img.shape[1]//2, img.shape[0]//2),(img.shape[1]//2 + 50, img.shape[0]//2 + 55),255,-1)
cv.imshow("mask",masks)

masked_img = cv.bitwise_and(img,img, mask= masks)
cv.imshow("masked",masked_img)
cv.waitKey(0)