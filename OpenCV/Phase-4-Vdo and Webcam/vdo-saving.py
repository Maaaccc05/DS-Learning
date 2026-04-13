# syntax ---> cv2.VideoWriter(filename, codec, fps, frame_size)  codec---> compression format, fps ---> frames per second

import cv2

camera = cv2.VideoCapture(0)

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID') # for mp4 format, you can also use 'XVID' for avi format
recorded = cv2.VideoWriter("myvideo.mp4", codec, 24, (frame_width, frame_height))

while True:
    success, image = camera.read()
    
    if not success:
        break

    recorded.write(image)
    cv2.imshow("Recorded", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

camera.release()
recorded.release()

cv2.destroyAllWindows()