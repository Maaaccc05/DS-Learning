# Syntax: cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

import cv2

image = cv2.imread("OpenCV/landscape-lake-mountain-clear-nature-wallpaper-preview.jpg")

blur = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Original",image)
cv2.imshow("Blurr", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()