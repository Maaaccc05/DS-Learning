import cv2
image = cv2.imread("OpenCV/dmxffni837f1xrj8pki9xgrl.jpg")

if image is None:
    print("Not found")

else:
    print("Image Loaded")
    pt1 = (50,50)
    pt2 = (400, 55)
    color = (0, 0, 255)
    thickness = 5

    cv2.line(image, pt1,pt2, color, thickness)

    cv2.imshow("Line image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Drawing rectangle 
# syntax: cv2.rectangle(image, pt1, pt2, color, thickness)

if image is None:
    print("Not found")

else:
    print("Image Loaded")
    pt1 = (250, 30)
    pt2 = (600, 350)
    color = (0, 0, 255)
    thickness = 3

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Drawing Circle
# Syntax: cv2.circle(imgae, center, radius, color, thickness)

if image is None:
    print("Not found")

else:
    print("Image Loaded")
    center = (400, 200)
    radius = 200
    color = (0, 0, 255)
    thickness = 3  # thickness can be -1 if you want to fill your cicle

    cv2.circle(image, center, radius, color, thickness)

    cv2.imshow("Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Adding Text
# syntanx: cv2.putText(image, text, org, font, fontScale, color, thickness)

if image is None:
    print("Not found")

else:
    print("Image Loaded")

    cv2.putText(image, "Hello OpenCV", (250, 400), cv2.FONT_HERSHEY_COMPLEX, 1.3, (0, 200, 255))

    cv2.imshow("Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()