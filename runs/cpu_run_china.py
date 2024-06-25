from ultralytics import YOLO
import pygetwindow as gw
import pyautogui
import cv2
import numpy as np
from pynput import keyboard
import time
import pydirectinput
import torch
import mss

model = YOLO("best.pt")

window_title = "反恐精英：全球攻势"
windows = gw.getWindowsWithTitle(window_title)
if not windows:
    raise Exception(f"无法找到名为'{window_title}'的游戏窗口")

window = windows[0]

mouse_move_enabled = False

notification_text = ""
notification_display_time = 2 
notification_start_time = None

def on_press(key):
    global mouse_move_enabled ,notification_text, notification_start_time
    try:
        if key.char == 't':
            mouse_move_enabled = not mouse_move_enabled

            notification_text = f"Mouse Move Enabled: {mouse_move_enabled}"
            notification_start_time = time.time()
            print(notification_text)
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

sct = mss.mss()

while True:
    start_time = time.time()
    
    monitor = {"top": window.top, "left": window.left, "width": window.width, "height": window.height}
    screenshot = sct.grab(monitor)

    img = np.array(screenshot)

    img = img[..., :3]

    target_resolution = (480, 270)
    img_resized = cv2.resize(img, target_resolution)
    
    results = model(img_resized)

    result = results[0] 

    for bbox in result.boxes.xyxy:
        x1, y1, x2, y2 = map(int, bbox)

        scale_x = window.width / target_resolution[0]
        scale_y = window.height / target_resolution[1]
        x1 = int(x1 * scale_x)
        y1 = int(y1 * scale_y)
        x2 = int(x2 * scale_x)
        y2 = int(y2 * scale_y)

        label = result.names[int(result.boxes.cls[np.where(result.boxes.xyxy == bbox)[0][0]])]

        if label == 'ct_body':
            mouse_x, mouse_y = pyautogui.position()
 
            target_center_x = window.left + (x1 + x2) // 2
            target_center_y = window.top + (y1 + y2) // 2

            x_offset = target_center_x - mouse_x
            y_offset = target_center_y - mouse_y

            if mouse_move_enabled:
                pydirectinput.moveRel(x_offset, y_offset, relative=True)
            break

    detected_img = result.plot()

    scale_factor = 2
    detected_img = cv2.resize(detected_img, (int(detected_img.shape[1] * scale_factor), int(detected_img.shape[0] * scale_factor)))

    if notification_text and time.time() - notification_start_time < notification_display_time:

        overlay = detected_img.copy()
        cv2.rectangle(overlay, (10, 10), (350, 60), (0, 0, 0), -1)
        alpha = 0.4 
        cv2.addWeighted(overlay, alpha, detected_img, 1 - alpha, 0, detected_img)
 
        cv2.putText(detected_img, notification_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)   

    cv2.imshow("YOLOv8 Detection on CS:GO", detected_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elapsed_time = time.time() - start_time
    sleep_time = max(0, 0.2 - elapsed_time)
    time.sleep(sleep_time)

cv2.destroyAllWindows()
listener.stop()