from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMenu

class OwlWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.is_ghost = False
        self.is_locked = False
        self.drag_offset = None
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        idle = QPixmap("assets/owl_idle.png")
        self.setPixmap(idle)
        self.resize(128,128)
        screen = QApplication.primaryScreen().availableGeometry()
        gap = 2
        x = screen.x() + gap
        y = screen.y() + screen.height() - self.height() - gap
        self.move(x, y)
        
    def mousePressEvent(self, event):
        self.drag_offset = event.globalPosition().toPoint() - self.pos()
    
    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and not self.is_locked:
            if self.drag_offset != None:
                point = event.globalPosition().toPoint() - self.drag_offset
                self.move(point)
    
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        ghost_action = menu.addAction("Ghost mode")
        locked_action = menu.addAction("Lock")
        ghost_action.setCheckable(True)
        locked_action.setCheckable(True)
        ghost_action.setChecked(self.is_ghost)
        locked_action.setChecked(self.is_locked)
        chosen = menu.exec(event.globalPos())
        if chosen == ghost_action:
            self.is_ghost = not self.is_ghost
            if self.is_ghost == True:
                self.setWindowOpacity(0.4)
            else:
                self.setWindowOpacity(1.0)
        if chosen == locked_action:
            self.is_locked = not self.is_locked
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            QApplication.quit()