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


def detect_with_yolo(image):
    results = model(image)
    cars = []
    pedestrians = []
    trucks = []

    for detection in results.xyxy[0]:
        label = int(detection[-1])
        if label == 2:  # Label for cars
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            cars.append(((x_min, y_min), (x_max, y_max), conf))
        elif label == 0:  # Label for pedestrians
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            pedestrians.append(((x_min, y_min), (x_max, y_max), conf))
        elif label == 7:  # Label for traffic lights
            x_min, y_min, x_max, y_max = map(int, detection[:4])
            conf = float(detection[4])
            trucks.append(((x_min, y_min), (x_max, y_max), conf))

    for car in cars:
        cv2.rectangle(image, car[0], car[1], (0, 0, 255), 2)

    for pedestrian in pedestrians:
        cv2.rectangle(image, pedestrian[0], pedestrian[1], (255, 0, 0), 2)

    for truck in trucks:
        cv2.rectangle(image, truck[0], truck[1], (0, 255, 0), 2)

    return image
