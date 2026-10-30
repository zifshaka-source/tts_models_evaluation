
import pygetwindow as gw
import pyperclip
from PIL import ImageGrab
import time
import threading
from datetime import datetime

class OSPerception:
    def __init__(self):
        self.current_window = ""
        self.current_clipboard = ""
        self.last_screenshot_path = "symbot_core/perception/last_screen.png"
        self.is_monitoring = True

    def get_active_window(self):
        try:
            window = gw.getActiveWindow()
            return window.title if window else "Unknown"
        except Exception:
            return "Unknown"

    def get_clipboard(self):
        try:
            return pyperclip.paste()
        except Exception:
            return ""

    def capture_screen(self):
        try:
            screenshot = ImageGrab.grab()
            screenshot.save(self.last_screenshot_path)
            return self.last_screenshot_path
        except Exception as e:
            print(f"Screenshot error: {e}")
            return None

    def monitor_loop(self):
        """Background loop to keep context updated."""
        while self.is_monitoring:
            self.current_window = self.get_active_window()
            self.current_clipboard = self.get_clipboard()
            # We only capture screen on specific triggers to save resources
            time.sleep(2) 

    def get_current_context(self):
        return {
            "active_window": self.current_window,
            "clipboard": self.current_clipboard,
            "timestamp": datetime.now().isoformat()
        }

    def start(self):
        self.thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.thread.start()
