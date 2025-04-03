from pyautogui import screenshot
from pyzbar.pyzbar import decode

class Qr_code:
    def __init__(self):
        self.screen = screenshot()
        self.qr_codes = self._decode(self.screen)

    def _decode(self, image):
        return decode(image)

    def output_data(self):
        for i in self.qr_codes:
            print(i.data.decode("utf-8"))


def main():
    qrcode = Qr_code()
    qrcode.output_data()
