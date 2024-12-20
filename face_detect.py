import cv2 as cv 

img = cv.imread("pics/group 1.jpg")



gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=2)

print(f'Number of faces in the image = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0),thickness=2)
cv.imshow("girl", img)
cv.waitKey(0)