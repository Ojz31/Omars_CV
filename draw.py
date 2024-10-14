import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3),dtype='uint8')

#rectangle
# cv.rectangle(blank, (blank.shape[1]//2 , blank.shape[0]//2), (40,40), (255,255,255), thickness = 2)

# cv.imshow('rect',blank)

# #circle
# cv.circle(blank,(225,225), 40, (225,225,225), thickness=cv.FILLED)
# cv.imshow('circle',blank)
# cv.waitKey(0)

#text 

cv.putText(blank, "Omar likes Allie <3", (20,225), cv.FONT_HERSHEY_COMPLEX, 1, (225,0,0), 2)
cv.imshow("text", blank)
cv.waitKey(0)