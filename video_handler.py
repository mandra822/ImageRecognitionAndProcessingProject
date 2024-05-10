import cv2


# Function to extract frames
def frameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    if not vidObj.isOpened():
        print("Error opening video file")
        return
    # Used as counter variable
    count = 0

    while True:
        success, image = vidObj.read()

        # Checks if frame was read successfully
        if not success:
            print("Error opening video file")
            break

        # Displays the frame in a window named "Frame"
        cv2.imshow("Project RiPO", image)

        # Waits for 25 milliseconds. If any key is pressed, it breaks out of the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Releases video object and closes all OpenCV windows
    vidObj.release()
    cv2.destroyAllWindows()




