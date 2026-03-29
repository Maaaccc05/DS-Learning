import cv2

image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is None:
    print("Error")
else:
    print("Image loaded")
