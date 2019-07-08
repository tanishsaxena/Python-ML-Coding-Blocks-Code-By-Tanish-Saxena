import cv2 

cap=cv2.VideoCapture(0)

while True:
	img=cv2.read()

	cv2.imshow(img)
	if waitKey(1)>30:
		break
cap.release()
cv2.deleteAllWindows()