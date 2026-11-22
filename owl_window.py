import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel

class OwlWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.Tool)
        idle = QPixmap("assets/owl_idle.png")
        self.setPixmap(idle)
        self.resize(128,128)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
