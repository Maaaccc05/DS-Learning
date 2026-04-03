import cv2

file_path = input("Enter Your file location")

image = cv2.imread(file_path)

choice = input("1.Type 'line' for drawing line on image\n2.Type 'rectangle' to draw rectangle on image\n3.Type 'circle' to draw circle on image\n4.Type 'text' to add tect on image ").lower()

if choice == 'line':
    x1 = int(input("Enter x1 value"))
    y1 = int(input("Enter y1 value"))
    pt1 = (x1, y1)
    x2 = int(input("Enter x2 value"))
    y2 = int(input("Enter y2 value")) 
    pt2 = (x2, y2)
    b = int(input("Enter B value of the color"))
    g = int(input("Enter G value of the color"))
    r = int(input("Enter R value of the color"))
    color = (b, g, r)
    thickness = int(input("Choose thickness"))
    cv2.line(image, pt1,pt2, color, thickness)

    cv2.imshow("Line On Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Wrong text")
