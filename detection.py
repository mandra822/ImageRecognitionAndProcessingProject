import cv2
import torch
import configurator as config

car_cascade = cv2.CascadeClassifier('./models/cars.xml')
pedestrian_cascade = cv2.CascadeClassifier('./models/haarcascade_fullbody.xml')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


def detect_objects(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    cars = car_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    pedestrians = pedestrian_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image


def detect_with_yolo(image, confidence_threshold):
    results = model(image)
    cars = []
    pedestrians = []
    trucks = []

    cars_color = config.cars_color
    pedestrians_color = config.pedestrians_color
    trucks_color = config.trucks_color

    cars_color_bgr = (cars_color[2], cars_color[1], cars_color[0])
    pedestrians_color_bgr = (pedestrians_color[2], pedestrians_color[1], pedestrians_color[0])
    trucks_color_bgr = (trucks_color[2], trucks_color[1], trucks_color[0])

    for detection in results.xyxy[0]:
        label = int(detection[-1])
        if label == 2 and config.detect_cars:  # Label for cars
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            cars.append(((x_min, y_min), (x_max, y_max), conf, "car", cars_color_bgr))
        elif label == 0 and config.detect_pedestrians:  # Label for pedestrians
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            pedestrians.append(((x_min, y_min), (x_max, y_max), conf, "person", pedestrians_color_bgr))
        elif label == 7 and config.detect_trucks:  # Label for trucks
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            trucks.append(((x_min, y_min), (x_max, y_max), conf, "truck", trucks_color_bgr))

    objects_to_detect = cars + pedestrians + trucks
    objects_to_detect = [x for x in objects_to_detect if x[2] >= confidence_threshold]

    for obj in objects_to_detect:
        (x_min, y_min), (x_max, y_max), conf, name,  color = obj
        mark_object(image, (x_min, y_min), (x_max, y_max), conf, name, color)

    return image, objects_to_detect


def mark_object(image, top_left, bottom_right, conf, name, color):
    cv2.rectangle(image, top_left, bottom_right, color, 2)
    cv2.putText(image, f"{name} {round(conf,2)}", (top_left[0], top_left[1]-3), cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.LINE_AA)
