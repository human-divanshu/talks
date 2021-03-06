import cv2
import numpy as np

img = cv2.imread("pc.jpg")
newimg = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

# skin filter
lower = np.array([120,120,100], np.uint8) # 0, 133, 77
upper = np.array([250,200,255], np.uint8)  #255, 173, 127

winName1 = "Original image"
winName2 = "Filtered image"

mask = cv2.inRange(newimg, lower, upper)
res = cv2.bitwise_and(img, img, mask=mask)


cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, img)
cv2.imshow(winName2, res)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
