import sys
from PySide6.QtWidgets import QApplication, QLabel
from owl_window import OwlWindow

app = QApplication(sys.argv)
owl= OwlWindow()
owl.show()
app.exec()
