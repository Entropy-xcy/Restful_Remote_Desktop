import base64
from PIL import Image
import numpy as np
import cv2
import requests
import io


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

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


if __name__ == "__main__":
    s0 = Server('localhost', 80)
    cv2.imshow("a", s0.get_screen())
    cv2.waitKey()
