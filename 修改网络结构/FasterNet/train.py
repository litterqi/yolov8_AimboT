#coding:utf-8
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8-FasterNet.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='datasets/TomatoData/data.yaml', epochs=50, batch=4)
