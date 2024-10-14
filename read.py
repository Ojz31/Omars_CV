import cv2 as cv

# img = cv.imread('pics/cat_large.jpg')

# cv.imshow('Cat', img)

# cv.waitKey(0)

video = cv.VideoCapture('videos/dog.mp4')

while video.isOpened():
    isTrue, frame = video.read()
    if not isTrue:
        break
    cv.imshow('video',frame)
    if cv.waitKey(10) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()