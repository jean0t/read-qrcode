import os
import shutil
from abc import ABC, abstractmethod
from subprocess import run, CalledProcessError
from tempfile import NamedTemporaryFile
from pathlib import Path
from io import BytesIO


from PIL import Image
import mss

class Screenshot(ABC):
    @abstractmethod
    def take_screenshot(self):
        pass
    
    def _convert_bytes_to_img(self, _bytes) -> Image.Image:
        img = Image.open(BytesIO(_bytes))
        return img

class WaylandScreenshot(Screenshot):
    def __init__(self):
        # needed due to wayland mess
        # why don't it simply has a screenshot tool that works anywhere like xorg?
        # D:
        self.desktop = (os.environ.get("XDG_CURRENT_DESKTOP") or os.environ.get("DESKTOP_SESSION") or "").lower()

    def take_screenshot(self) -> Image.Image:
        try:
            if shutil.which("wayshot"):
                result = run(["wayshot", "-f", "-"], capture_output=True, check=True)
                img = self._convert_bytes_to_img(result.stdout)
                return img

            elif "kde" in self.desktop:
                with NamedTemporaryFile(suffix=".png", delete=True) as tmpfile:
                    path = Path(tmpfile.name)
                    run(["spectacle", "-n", "-b", "-o", path.__str__()], check=True)
                    result = path.read_bytes()
                img = self._convert_bytes_to_img(result)
                return img

            elif "gnome" in self.desktop:
                with NamedTemporaryFile(suffix=".png", delete=True) as tmpfile:
                    path = Path(tmpfile.name)
                    run(["gnome-screenshot", path.__str__()], check=True)
                    result = path.read_bytes()
                img = self._convert_bytes_to_img(result)
                return img

            else:
                result = run(["grim", "-"], capture_output=True, check=True)
                img = self._convert_bytes_to_img(result.stdout)
                return img

        except CalledProcessError as e:
            print("failed to capture screenshot: ", e)
            exit(1)

class XorgScreenshot(Screenshot):
    def take_screenshot(self) -> Image.Image:
        with mss.mss() as screen:
            monitor = screen.monitors[1] # current monitor
            screenshot = screen.grab(monitor)
            img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
            return img


class ScreenshotFactory:
    @staticmethod
    def create_screenshot() -> Screenshot:
        compositor = os.environ.get("XDG_SESSION_TYPE").lower()
        if compositor == "wayland":
            return WaylandScreenshot()
        
        else:
            return XorgScreenshot()

