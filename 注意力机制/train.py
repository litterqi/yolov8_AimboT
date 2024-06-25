from ultralytics import YOLO

model=YOLO('ultralytics\cfg\models/v8\yolov8_CBAM.yaml')

model.train(data='coco128.yaml',workers=0,epochs=2,batch=4)