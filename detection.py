import cv2
import torch

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

    for detection in results.xyxy[0]:
        label = int(detection[-1])
        if label == 2:  # Label for cars
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            cars.append(((x_min, y_min), (x_max, y_max), conf, "car", (0, 0, 255)))
        elif label == 0:  # Label for pedestrians
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            pedestrians.append(((x_min, y_min), (x_max, y_max), conf, "person", (0, 255, 0)))
        elif label == 7:  # Label for trucks
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            trucks.append(((x_min, y_min), (x_max, y_max), conf, "truck", (255, 0, 0)))

    objects_to_detect = cars + pedestrians + trucks
    objects_to_detect = [x for x in objects_to_detect if x[2] >= confidence_threshold]

    for obj in objects_to_detect:
        (x_min, y_min), (x_max, y_max), conf, name,  color = obj
        mark_object(image, (x_min, y_min), (x_max, y_max), conf, name, color)

    return image


def mark_object(image, top_left, bottom_right, conf, name, color):
    cv2.rectangle(image, top_left, bottom_right, color, 2)
    cv2.putText(image, f"{name} {round(conf,2)}", (top_left[0], top_left[1]-3), cv2.FONT_HERSHEY_PLAIN, 1, color, 1, cv2.LINE_AA)
