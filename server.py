from flask import Flask
from flask import request
import pyautogui
import numpy as np
import cv2
import base64

app = Flask(__name__)


# Return the size of the screen
@app.route('/get_screen_size')
def get_screen_size():
    image = pyautogui.screenshot()
    image = np.array(image)
    return str(len(image[0]))+'*'+str(len(image))


# Return the string of base64 containing the image
@app.route('/get_screen')
def get_screen():
    image = pyautogui.screenshot()
    image = np.array(image)

    # Encode into JPG
    ret, image_jpg = cv2.imencode(".jpg", image)

    # Convert to Base 64
    image_base64 = base64.b64encode(image_jpg)
    b64_str = image_base64.decode()
    return b64_str


# Move the cursor relative to the current position
@app.route('/move_cursor')
def move_cursor():
    del_x = request.args.get('del_x', default=0, type=int)
    del_y = request.args.get('del_y', default=0, type=int)
    duration = request.args.get('duration', default=0, type=float)
    pyautogui.moveRel(del_x, del_y, duration)
    return "0"


@app.route('/move_cursor_to')
def move_cursor_to():
    x = request.args.get('x', default=0, type=int)
    y = request.args.get('y', default=0, type=int)
    duration = request.args.get('duration', default=0, type=float)
    pyautogui.moveTo(x, y, duration)
    return "0"


@app.route('/mouse_key')
def mouse_key():
    # key could be 'left' 'middle' 'right'
    key = request.args.get('key', default='left', type=str)
    # event could be 'down' 'up' 'click'
    event = request.args.get('event', default='click', type=str)
    if event == 'click':
        if key == 'left':
            pyautogui.click()
        elif key == 'middle':
            pyautogui.middleClick()
        elif key == 'right':
            pyautogui.rightClick()
    elif event == 'down':
        pyautogui.mouseDown(button=key)
    elif event == 'up':
        pyautogui.mouseUp(button=key)

    return "0"


@app.route('/key_down')
def key_down():
    key = request.args.get('key', default='', type=str)
    pyautogui.keyDown(key)
    return "0"


@app.route('/key_up')
def key_up():
    key = request.args.get('key', default='', type=str)
    pyautogui.keyUp(key)
    return "0"


@app.route('/type_write')
def type_write():
    message = request.args.get('message', default='', type=str)
    delay = request.args.get('delay', default=0, type=float)
    pyautogui.typewrite(message, delay)
    return "0"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
