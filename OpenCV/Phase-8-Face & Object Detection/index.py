import cv2

face_cascade = cv2.CascadeClassifier("OpenCV/Phase-8-Face & Object Detection/haarcascade_frontalcatface.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale()