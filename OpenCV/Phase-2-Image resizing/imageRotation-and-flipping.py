# Syntax for image ratation
# M = cv2.getRotationMatrix2D(Center, Angle, Scale)
# roatated_image = cv2.warpAffine(image, M, (widht, height))


# (0,0) ------------------------> width(x)
#       |
#       |                   center point = (width // 2, height // 2)
#       |
#      Height(Y)

import cv2
image = cv2.imread("OpenCV/minato-namikaze-3840x2160-24353.png")

if image is None:
    print("Could Not Found")
else:
    resized = cv2.resize(image, (500, 500))
    (h,w) = resized.shape[:2]
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(resized, M, (w,h))

    cv2.imshow("90 degree Rotation", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Image Flipping

if image is None:
    print("Could not load")
else:
    resized = cv2.resize(image, (500, 500))

    flipped_horizontal = cv2.flip(resized, 1)
    flipped_vertical = cv2.flip(resized, 0)
    both_flip = cv2.flip(resized, -1)

    cv2.imshow("Original", resized)
    cv2.imshow("Horizontal", flipped_horizontal)
    cv2.imshow("Vertical", flipped_vertical)
    cv2.imshow("Both", both_flip)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

