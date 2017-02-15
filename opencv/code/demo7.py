import cv2
import numpy as np


img = cv2.imread("obama.jpg")
bg = cv2.imread("background.jpg")

# height and width
x, y, c = img.shape

af = 45

for i in range(0, x):
    for j in range(0, y):
        b = img[i,j][0]
        g = img[i,j][1]
        r = img[i,j][2]
        if g > b + af and g > r + af:
            img[i,j] = bg[i,j]

winName1 = "Obama on moon"

cv2.startWindowThread()
cv2.namedWindow(winName1)
cv2.imshow(winName1, img)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
