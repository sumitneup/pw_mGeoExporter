from imports import *


class attribTableWidgetClass(QWidget):
    def __init__(self):
        super(attribTableWidgetClass, self).__init__()
        self.ly = QHBoxLayout()
        self.setLayout(self.ly)