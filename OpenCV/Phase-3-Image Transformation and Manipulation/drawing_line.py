import cv2
image = cv2.imread("OpenCV/dmxffni837f1xrj8pki9xgrl.jpg")

# if image is None:
#     print("Not found")

# else:
#     print("Image Loaded")
#     pt1 = (50,50)
#     pt2 = (400, 55)
#     color = (0, 0, 255)
#     thickness = 5

#     cv2.line(image, pt1,pt2, color, thickness)

#     cv2.imshow("Line image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

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