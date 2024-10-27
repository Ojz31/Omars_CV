import numpy as np 
import cv2 as cv 
import os
haar_cascade = cv.CascadeClassifier('haar_face.xml')


p = [person for person in os.listdir(r'F:\coding\CV\data\train')]


# features = np.load('features.npy',allow_pickle=True)
# labels = np.load('labels.npy')

faces_recongnizer = cv.face.LBPHFaceRecognizer_create()
faces_recongnizer.read('face_trained.yml')

img = cv.imread('F:\\coding\\CV\\data\\val\\arnold_schwarzenegger\\379px-Arnold_Schwarzenegger_-_2019_(33730956438)_(cropped).jpg')

cv.imshow("color",img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("person",gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = faces_recongnizer.predict(faces_roi)
    print(f'Label = {p[label]} with confidence score {confidence}')

    cv.putText(img, str(p[label]), (20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), thickness=2)
    cv.rectangle(img, (x,y),(x+w,y+h), (0,255,0),thickness=2)

cv.imshow('detected face',img)

cv.waitKey(0)