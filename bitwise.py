import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(20,20),(350,350),255,-1)
cv.imshow("rectangle",rectangle)

circle = cv.circle(blank.copy(),(250,250),200,255,-1)
cv.imshow("circle",circle)

bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow("and",bit_and)

bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow("or",bit_or)

bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("xor",bit_xor)



cv.waitKey(0)