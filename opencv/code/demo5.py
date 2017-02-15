import cv2
import numpy as np

img = cv2.imread("cutecat.jpeg")

# will return height, width and channel number
x, y, c = img.shape


newimg = cv2.resize(img, (y*2, x*2))

winName1 = "Cute cat"
winName2 = "Cutet cat resize"

cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, img)
cv2.imshow(winName2, newimg)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
