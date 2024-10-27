import os
import cv2 as cv
import numpy as np


p = [person for person in os.listdir(r'F:\coding\CV\data\train')]

haar_cascade = cv.CascadeClassifier('haar_face.xml')


DIR = r'F:\coding\CV\data\train'

features = []
labels = []

def create_train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            print(f"Processing: {img_path}")

            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Warning: Failed to load {img_path}")
                continue 

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


create_train()

print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')
features = np.array(features,dtype='object')
labels = np.array(labels)

faces_recongnizer = cv.face.LBPHFaceRecognizer_create()

faces_recongnizer.train(features,labels)

faces_recongnizer.save('face_trained.yml')
np.save('features.npy',features)
np.save('labels.npy', labels)