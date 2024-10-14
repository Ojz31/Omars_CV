import cv2 as cv
import numpy as np 

img = cv.imread("pics/park.jpg")
#cv.imshow("park",img)

#transformation

def transform(img, x,y):
    mat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, mat,dim)

transformed = transform(img,-100,-200)
cv.imshow("transformed",transformed)

def rotation(img, angle , rotationPoint = None):
    (height,width) = img.shape[:2]
    if rotationPoint == None:
        rotationPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotationPoint , angle , 1)
    dim = (width,height)

    return cv.warpAffine(img,rotMat,dim)

rotationpic = rotation(img,45)
cv.imshow("rotation", rotationpic)

#flipping
flipped = cv.flip(img, 1)
cv.imshow("flipped",flipped)
cv.waitKey(0)