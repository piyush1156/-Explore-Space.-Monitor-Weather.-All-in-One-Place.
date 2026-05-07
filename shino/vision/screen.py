import mss
import numpy as np
import cv2
import pytesseract
from shino.core.logger import logger

class ScreenAnalyzer:
    def __init__(self):
        self.sct = mss.mss()

    def capture_screen(self):
        monitor = self.sct.monitors[1]
        screenshot = self.sct.grab(monitor)
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    def extract_text(self, image=None):
        if image is None:
            image = self.capture_screen()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        return text

    def detect_errors(self, text: str):
        error_keywords = ["SyntaxError", "Traceback", "Exception", "Error", "failed to compile"]
        found_errors = [kw for kw in error_keywords if kw in text]
        return found_errors

screen_analyzer = ScreenAnalyzer()
