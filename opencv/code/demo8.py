import cv2

img = cv2.imread("dirty.jpg")

ret, newimg = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)

winName1 = "Original image"
winName2 = "Thresholded image"

cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, img)
cv2.imshow(winName2, newimg)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
