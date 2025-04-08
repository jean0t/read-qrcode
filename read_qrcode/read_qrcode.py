from subprocess import run
from os import environ
from io import BytesIO

from pyautogui import screenshot
from pyzbar.pyzbar import decode
from PIL import Image

class Qr_code:
    def __init__(self):
        self.screen = self._take_screenshot()
        self.qr_codes = self._decode(self.screen)

    def _take_screenshot(self):
        session_type = environ.get("XDG_SESSION_TYPE")
        if session_type.lower() == "x11":
            return screenshot()
        
        elif session_type.lower() == "wayland":
            screen_image = run(['flameshot', 'screen', '-r'], capture_output=True)
            
            if screen_image.returncode == 0:
                return Image.open(BytesIO(screen_image.stdout))
            else:
                print(screen_image.stderr)
                exit(screen.returncode)

    def _decode(self, image):
        return decode(image)

    def output_data(self):
        for i in self.qr_codes:
            print(i.data.decode("utf-8"))


