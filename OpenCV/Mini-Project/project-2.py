import cv2

file_path = input("Enter Your file location: ")

image = cv2.imread(file_path)

if image is None:
    print("Image not found")
    exit()

choice = input("1.Type 'line' for drawing line on image\n2.Type 'rectangle' to draw rectangle on image\n3.Type 'circle' to draw circle on image\n4.Type 'text' to add text on image\n").lower()

def get_points_1():
    x1 = int(input("Enter x1 value: "))
    y1 = int(input("Enter y1 value: "))
    return(x1, y1)

def get_points_2():
    x2 = int(input("Enter x2 value: "))
    y2 = int(input("Enter y2 value: "))
    return(x2, y2)

def get_color():
    b = int(input("B: "))
    g = int(input("G: "))
    r = int(input("R: "))
    return (b, g, r)

def get_thickness():
    thick = int(input("Enter Thickness: "))
    return(thick)

def dest_disp():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if choice == 'line':
    pt1 = get_points_1()
    pt2 = get_points_2()
    color = get_color()
    thickness = int(input("Choose thickness"))
    cv2.line(image, pt1,pt2, color, thickness)

    cv2.imshow("Line On Image", image)
    dest_disp()

elif choice == 'rectangle':
    pt1 = get_points_1()
    pt2 = get_points_2()
    color = get_color()
    thickness = get_thickness()

    cv2.rectangle(image, pt1, pt2, color, thickness)
    cv2.imshow("Rectangle On Image", image)
    dest_disp()

elif choice == 'circle':
    x1 = int(input("Enter x1 value: "))
    y1 = int(input("Enter y1 value: "))
    center = (x1, y1)
    radius = int(input("Enter Radius of the circle: "))
    color = get_color()
    thickness = get_thickness()

    cv2.circle(image, center, radius, color, thickness)
    cv2.imshow("Circle On Image", image)
    dest_disp()

elif choice == 'text':
    text = input("Enter your text you want to add on img: ")
    x = int(input("Enter x Value: "))
    y = int(input("Enter y Value: "))
    org = (x, y)
    font = cv2.FONT_HERSHEY_COMPLEX
    fontScale = float(input("Enter Font Scale of the text: "))
    color = get_color()
    thickness = get_thickness()

    cv2.putText(image, text, org, font, fontScale, color, thickness)
    cv2.imshow("Text on img", image)
    dest_disp()

else:
    print("Invalid Text")