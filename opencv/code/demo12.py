import cv2
import numpy as np

img = cv2.imread("obama.jpg")
newimg = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

lower = np.array([0,133,77], np.uint8)
upper = np.array([255,173,127], np.uint8) 

winName1 = "Original image"
winName2 = "Filtered image"

mask = cv2.inRange(newimg, lower, upper)
res = cv2.bitwise_and(img, img, mask=mask)

kernel = np.ones((18,18), np.float32)/255
smoothed = cv2.filter2D(res, -1, kernel)

cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, img)
cv2.imshow(winName2, smoothed)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
