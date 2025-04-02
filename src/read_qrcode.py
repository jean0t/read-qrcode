import pyautogui as pag
import numpy as np
from cv2 import COLOR_RGB2BGR, cvtColor, QRCodeDetector

def main():
    screenshot = pag.screenshot()
    screenshot = np.array(screenshot)
    screenshot = cvtColor(screenshot, COLOR_RGB2BGR)

    qr_decoder = QRCodeDetector()
    retval, decoded_info, _, _ = qr_decoder.detectAndDecodeMulti(screenshot)
    if retval:
        for n, i in enumerate(decoded_info):
            print(f"{n+1}º ", i)
    else:
        print("")

if __name__ == '__main__':
    main()
