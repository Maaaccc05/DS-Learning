import cv2
image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is None:
    print("Not found")

else:
    resized = cv2.resize(image, (500, 500))
    print("Image Loaded")
    pt1 = (50,50)
    pt2 = (400, 55)
    color = (0, 0, 255)
    thickness = 5

    cv2.line(resized, pt1,pt2, color, thickness)

    cv2.imshow("Line image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()