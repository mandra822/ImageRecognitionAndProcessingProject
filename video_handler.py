import cv2
import detection
from line_drawer import draw_parking_line, check_if_intersect, get_line_end_point
import tkinter as tk
from PIL import Image, ImageTk
import configurator as config
import default_settings

line_angle = default_settings.line_angle

def show_frame(video, label, scale, confidence):
    success, image = video.read()
    if not success:
        print("Error - End of video")
        return

    resized_image = cv2.resize(image, None, fx=scale, fy=scale)
    image_with_detection, detected_objects = detection.detect_with_yolo(resized_image, confidence)

    if config.lines_displayed:
        shape = image_with_detection.shape
        line1_pivot = (int(shape[0] / 3), 0)
        line2_pivot = (int(shape[0]), 0)
        line_length = 250
        line_color = config.lines_color

        line1_end = get_line_end_point(line1_pivot, line_angle, line_length)
        line2_end = get_line_end_point(line2_pivot, line_angle, line_length)

        is_intersection = False
        for obj in detected_objects:
            (x_min, y_min), (x_max, y_max), conf, name, color = obj
            is_intersection = check_if_intersect(line1_pivot, line1_end, (x_min, y_min), (x_max, y_max))
            if is_intersection:
                break
            is_intersection = check_if_intersect(line2_pivot, line2_end, (x_min, y_min), (x_max, y_max))
            if is_intersection:
                break

        if is_intersection:
            line_color = config.lines_color_alert
        draw_parking_line(image_with_detection, line1_pivot, line_angle, line_length, 2, line_color)
        draw_parking_line(image_with_detection, line2_pivot, line_angle, line_length, 2, line_color)

    img = Image.fromarray(cv2.cvtColor(image_with_detection, cv2.COLOR_BGR2RGB))
    imgTk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgTk
    label.configure(image=imgTk)
    label.after(10, lambda: show_frame(video, label, scale, confidence))

def frameCapture_with_yolo(path, scale=0.5, confidence=0.5):
    vidObj = cv2.VideoCapture(path)

    if not vidObj.isOpened():
        print("Error opening video file")
        return

    main_window = tk.Tk()
    main_window.title("Project RiPO")

    main_label = tk.Label(main_window)
    main_label.pack(pady=5)

    angle_scale = tk.Scale(main_window, from_=-90, to=90, length=270 ,orient=tk.HORIZONTAL)
    angle_scale.pack()

    def on_scale_change(value):
        global line_angle
        line_angle = value

    angle_scale.bind("<Motion>", lambda event: on_scale_change(angle_scale.get()))

    config_button = tk.Button(main_window, text="Open Configurator", command=lambda: config.open_config_window(main_window))
    config_button.pack(pady=10)

    show_frame(vidObj, main_label, scale, confidence)
    main_window.mainloop()

    vidObj.release()
    cv2.destroyAllWindows()


#old version
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