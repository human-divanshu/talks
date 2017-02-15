import cv2

cap = cv2.VideoCapture(0)

winName1 = "Live feed"
winName2 = "Grayscale"

cv2.startWindowThread()
cv2.namedWindow(winName1)
cv2.namedWindow(winName2)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow(winName1, frame)
    cv2.imshow(winName2, gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
