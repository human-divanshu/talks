import cv2

img = cv2.imread("cutecat.jpeg")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

winName1 = "Cute cat"
winName2 = "Cute cat gray"

cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


cv2.imshow(winName1, img)
cv2.imshow(winName2, grayimg)

# pressing any key will break GUI loop and close window
cv2.waitKey(0)

cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
