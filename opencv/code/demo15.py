import cv2

cap = cv2.VideoCapture(0)

winName1 = "Live feed"

cv2.startWindowThread()
cv2.namedWindow(winName1)


while True:
    ret, frame = cap.read()

    cv2.imshow(winName1, frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow(winName1)
