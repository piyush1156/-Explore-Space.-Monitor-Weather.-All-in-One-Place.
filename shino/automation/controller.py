import pyautogui
import keyboard
import mouse
import pygetwindow as gw
from shino.core.logger import logger
import time
import random

class DesktopController:
    def __init__(self):
        pyautogui.FAILSAFE = True

    def human_move_mouse(self, x, y):
        # Implementation of smooth, human-like mouse movement
        current_x, current_y = pyautogui.position()
        steps = 20
        for i in range(steps):
            tx = current_x + (x - current_x) * (i / steps) + random.randint(-2, 2)
            ty = current_y + (y - current_y) * (i / steps) + random.randint(-2, 2)
            pyautogui.moveTo(tx, ty)
            time.sleep(0.01)
        pyautogui.moveTo(x, y)

    def type_text(self, text):
        logger.info(f"Typing: {text}")
        pyautogui.write(text, interval=0.05)

    def press_key(self, key):
        pyautogui.press(key)

    def click(self, x=None, y=None):
        if x and y:
            self.human_move_mouse(x, y)
        pyautogui.click()

    def list_windows(self):
        return gw.getAllTitles()

    def activate_window(self, title):
        try:
            win = gw.getWindowsWithTitle(title)[0]
            win.activate()
            return True
        except Exception as e:
            logger.error(f"Failed to activate window {title}: {e}")
            return False

desktop_controller = DesktopController()
