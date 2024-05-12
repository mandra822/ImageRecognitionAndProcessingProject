import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

image = cv2.imread('./assets/ranczo.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = model(image, size=640)

results.print()
results.show()
  
print(results.pandas().xyxy[0])