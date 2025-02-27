from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout , QHBoxLayout , QPushButton # type: ignore
from PySide6.QtGui import QPixmap  # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("QLabel and Images")
        
        label = QLabel()
        label.setPixmap(QPixmap("Images/Brain.png"))

        layout = QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)