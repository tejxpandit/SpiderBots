# Project : SpiderBots
# File : Object Detector Class using YOLOv5
# Author : Tej Pandit
# Date : Jan 2024

import torch
import cv2

class ObjectDetector():

    def __init__(self):
        # Model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # Default Device GPU
        #model = torch.hub.load('ultralytics/yolov5', 'yolov5m', device="cpu") # Run with CPU  

    def detect(self, name, frame, display):
        img = cv2.resize(frame,(640,480))
        results = self.model(img)

        for box in results.xyxy[0]:
                print(box)
                if box[4]>0.5:
                    xB = int(box[2])
                    xA = int(box[0])
                    yB = int(box[3])
                    yA = int(box[1])
                    cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)

        if(display):
            cv2.imshow(name, img)

        return results

    def terminate(self):
        cv2.destroyAllWindows()