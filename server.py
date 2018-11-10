from flask import Flask
import pyautogui
import numpy as np
import cv2
import base64

app = Flask(__name__)


@app.route('/get_info')
def get_info():
    return "info"


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


@app.route('/move_cursor')
def move_cursor():
    return "move cursor"


@app.route('/left_down')
def left_down():
    return "cursor down"


@app.route('/left_up')
def left_up():
    return "cursor up"


@app.route('/move_cursor_to')
def move_cursor_to():
    return "move cursor to"


@app.route('/key_down')
def key_down():
    return "Key down"


@app.route('/key_up')
def key_up():
    return "keyup"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
