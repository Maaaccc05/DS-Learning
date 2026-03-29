import cv2

image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")


if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded: \nHeight: {h}\nWidth: {w}\n Channels: {c}")
else:
    print("Could Not load")
