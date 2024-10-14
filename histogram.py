import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img = cv.imread("pics/cats.jpg")
cv.imshow("cats",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)
blank = np.zeros(img.shape[:2],dtype="uint8")

circle = cv.circle(blank,(img.shape[1]//2, img.shape[0]//2),100,255,-1)

# masked = cv.bitwise_and(gray,gray,mask=circle)
# cv.imshow(",asked",masked)

# hist = cv.calcHist([gray],[0],masked,[256],[0,256])

# plt.figure()
# plt.title("Gray histogram")
# plt.xlabel("bins")
# plt.ylabel("No. of pixels")
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()

#hist for bgr
plt.figure()
plt.title("Gray histogram")
plt.xlabel("bins")
plt.ylabel("No. of pixels")
colors = ('b','g','r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])


plt.show()


cv.waitKey(0)