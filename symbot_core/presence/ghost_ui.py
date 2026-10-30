
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import Qt, Py signals

class GhostUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Make window transparent and always on top
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 400, 100)
        
        self.label = QLabel("Symbot: Idle", self)
        self.label.setStyleSheet("color: #60a5fa; font-size: 18px; font-weight: bold; font-family: 'Inter';")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 400, 100)

    def update_status(self, text):
        self.label.setText(f"Symbot: {text}")
        self.show()

    def hide_status(self):
        self.hide()
