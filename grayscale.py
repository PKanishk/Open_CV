import cv2
image = cv2.imread("C:/collage photos/collage guys/Snapchat-103534450.jpg")
cv2.imshow('Displayed Image', image) 
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("Grayscale",hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
