# Gaussian Blur Syntax: cv2.GaussianBlur(src, (kernel_size, kernel_size), sigma)

import cv2

# image = cv2.imread("OpenCV/landscape-lake-mountain-clear-nature-wallpaper-preview.jpg")

# blur = cv2.GaussianBlur(image, (21, 21), 5) # Can't pass even value it should be odd in kernel_size

# cv2.imshow("Original",image)
# cv2.imshow("Blurr", blur)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



# Median Blur Syntax : cv2.medianBlur(src, kernel_size)

img = cv2.imread("OpenCV/Blur-img2.jpeg")

med_blur = cv2.medianBlur(img, 3)

cv2.imshow("Original",img)
cv2.imshow("MedianBlur", med_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()



# Sharpening an Image Syntax: cv2.filter2D(src, ddepth, kernel)

