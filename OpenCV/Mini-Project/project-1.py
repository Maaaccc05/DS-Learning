import cv2

image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    input("Do you want to save or Show")
    if 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not convert")

