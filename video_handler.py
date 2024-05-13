import cv2
import detection


# Function to extract frames
def frameCapture(path, scale = 0.5):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    width = int(vidObj.get(3))
    height = int(vidObj.get(4))

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

        resized_image = cv2.resize(image, None, fx=scale, fy=scale)

        image_with_detection = detection.detect_objects(resized_image)

        # Displays the frame in a window named "Frame"
        cv2.imshow("Project RiPO", image_with_detection)

        # Waits for 25 milliseconds. If any key is pressed, it breaks out of the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        # Releases video object and closes all OpenCV windows
    vidObj.release()
    cv2.destroyAllWindows()


def frameCapture_with_yolo(path, scale=0.5, confidence=0.5):
    vidObj = cv2.VideoCapture(path)

    while vidObj.isOpened():
        success, image = vidObj.read()

        if not success:
            print("Error opening video file")
            break

        resized_image = cv2.resize(image, None, fx=scale, fy=scale)

        image_with_detection = detection.detect_with_yolo(resized_image, confidence)

        cv2.imshow('Project RiPo', image_with_detection)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    vidObj.release()
    cv2.destroyAllWindows()