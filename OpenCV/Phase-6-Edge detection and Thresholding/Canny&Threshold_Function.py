# Canny edge detection Syntax: cv2.Canny(src, threshold1, threshold2)

import cv2

# img = cv2.imread("OpenCV/Phase-6-Edge detection and Thresholding/BMW.jpg", cv2.IMREAD_GRAYSCALE)

# canny = cv2.Canny(img, 150, 50)

# cv2.imshow("Original", img)
# cv2.imshow("Canny", canny)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Syntax for Threshold: cv2.threshold(src, thresh_value, max_value, method)

img = cv2.imread("OpenCV/Phase-6-Edge detection and Thresholding/BMW.jpg", cv2.IMREAD_GRAYSCALE)

ret, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Thresholded", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()