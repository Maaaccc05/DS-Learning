import cv2

camera = cv2.VideoCapture(0)

Choice = int(input("1 for Capture and save Video in directory\n2 for Only Capture Video\n 3 for Capture video and open in VLC media player"))

def all_vdo_related():
    frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

    codec = cv2.VideoWriter_fourcc(*'XVID')
    if Choice == 1:
        recorded = cv2.VideoWriter("myvideo.avi", codec, 24, (frame_width, frame_height))

        while True:
            success, image = camera.read()

            if not success:
                break
        
            recorded.write(image)
            cv2.imshow("Soon will be Saving", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break
        camera.release()
        recorded.release()
        cv2.destroyAllWindows()
    elif Choice == 2:
        while True:
            ret, frame = camera.read()  # ret = True/false  frame = image

            if not ret:
                print("Could not found")
                break

            cv2.imshow("WebCam",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break

        camera.release()
        cv2.destroyAllWindows()
    else:
        print("wrong choice")

vid_saving()