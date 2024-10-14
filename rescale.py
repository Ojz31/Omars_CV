import cv2 as cv

def rescale(frame,scale = .75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img = cv.imread('pics/cat_large.jpg')

img_resize = rescale(img,.2)
cv.imshow('cat',img_resize)
cv.waitKey(0)

video = cv.VideoCapture('videos/dog.mp4')

while video.isOpened():
    isTrue, frame = video.read()
    frame_resized = rescale(frame,.2)
    if not isTrue:
        break
    cv.imshow('video',frame_resized)

    if cv.waitKey(20) & 0xFF == 'd':
        break

video.release()
cv.destroyAllWindows()
