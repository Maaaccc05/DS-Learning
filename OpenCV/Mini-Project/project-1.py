import cv2

image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is None:
    print("Error: Image not found")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

choice = input("Type 'show' to display and 'save' to Save the image ").lower()

if choice == "show":
    cv2.imshow("GrayScaled Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == "save":
    filename = input("Enter File name to save with (.png or .jpg)")

    cv2.imwrite(filename, gray)
    print("Image is saved as {filename}")

else:
    print("Invalid Choice type again")