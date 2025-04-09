from os import environ
from io import BytesIO

from .screenshot import ScreenshotFactory
from pyzbar.pyzbar import decode

class QrCode:
    def __init__(self):
        self.screenshot = ScreenshotFactory.create_screenshot()
        self.screen = self._get_image()
        self.qr_codes = self._decode(self.screen)

    def _get_image(self) -> Image:
        return self.screenshot.take_screenshot()

    def _decode(self, image):
        return decode(image)

    def output_data(self):
        for i in self.qr_codes:
            print(i.data.decode("utf-8"))


