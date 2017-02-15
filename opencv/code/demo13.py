import cv2
import numpy as np
import copy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread("ab.jpg")
original = copy.deepcopy(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)


winName1 = "Original image"
winName2 = "Filtered image"
cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, original)
cv2.imshow(winName2, img)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
