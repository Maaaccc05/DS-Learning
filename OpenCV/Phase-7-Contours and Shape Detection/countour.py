"""
    Syntax of Countours: contours, hierarchy = cv2.findContours(img, mode, method)
    Syntax for Draw Contoirs: cv2.drawContours(img, contours, contour_index, color, thickness)

    *** Shape Detection***
    syntax: cv2.apprpolyDP(curve, epsilon, True)

"""

import cv2
import numpy as np

img = cv2.imread("OpenCV/Phase-7-Contours and Shape Detection/triangle.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find Contours

contours, hirearchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        print("Unknown")
    
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0))


cv2.imshow("Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()