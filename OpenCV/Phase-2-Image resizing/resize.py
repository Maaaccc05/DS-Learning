import cv2
image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is None:
    print("Image not found")
else:
    print("Image is loaded")

    resized = cv2.resize(image, (300, 300))

    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
