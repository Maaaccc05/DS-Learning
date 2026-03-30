import cv2
image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is not None:
    cropped = image[100:200, 50:150]
    
