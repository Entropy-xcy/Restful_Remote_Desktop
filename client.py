import base64
from PIL import Image
import numpy as np
import time
import requests
import io


class Server:
    def __init__(self, host, port=80, display=True):
        self.host = host
        self.port = port
        if display:
            print(str(host) + ":" + str(port) + " Initializing...")
        self.width, self.height = self.get_screen_size()
        if display:
            print(str(host) + ":" + str(port) + " Initialized")
            print("Width:" + str(self.width) + "  Height:" + str(self.height))

    # Return the screen shot's base64 string
    def get_screen_base64(self):
        r = requests.get("http://" + str(self.host)
                         + ':' + str(self.port)
                         + '/get_screen')
        assert r.status_code == 200
        return r.text

    # Return the screen shot in cv format
    def get_screen(self):
        b64_str = self.get_screen_base64()
        img_data = base64.b64decode(b64_str)
        img = Image.open(io.BytesIO(img_data))
        img = np.array(img)
        return img

    # Return the screen size of the server
    def get_screen_size(self):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/get_screen_size'

        r = requests.get(url)
        assert r.status_code == 200
        size = r.text.split("*")
        width = int(size[0])
        height = int(size[1])
        return width, height

    # Move the cursor relative to current position on the server
    def move_cursor(self, del_x, del_y, duration=0):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/move_cursor'
        payload = {'del_x': str(del_x), 'del_y': str(del_y), "duration": str(duration)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"

    # Move the cursor to position (x,y)
    def move_cursor_to(self, x, y, duration=0):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/move_cursor_to'
        payload = {'x': str(x), 'y': str(y), "duration": str(duration)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"

    # Handle Mouse Key Event
    def mouse_key(self, key='left', event='click'):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/mouse_key'
        payload = {'key': str(key), 'event': str(event)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"

    # Keyboard down
    def key_down(self, key):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/key_down'
        payload = {'key': str(key)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"

    # Keyboard up
    def key_up(self, key):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/key_up'
        payload = {'key': str(key)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"

    # Type message
    def type_write(self, message, delay=0):
        url = "http://" + str(self.host) + ':' + str(self.port) + '/type_write'
        payload = {'message': str(message), 'delay': str(delay)}
        r = requests.get(url, params=payload)

        assert r.status_code == 200
        assert r.text == "0"


if __name__ == "__main__":
    s0 = Server('localhost', 80)
    time.sleep(2)
    s0.key_down('win')
    s0.key_down('r')
    s0.key_up('r')
    time.sleep(1)
    s0.key_up('win')
