import cv2

img = cv2.imread("cutecat.jpeg")

winName = "Cute cat"

cv2.startWindowThread()
cv2.namedWindow(winName)

cv2.imshow(winName, img)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName)
