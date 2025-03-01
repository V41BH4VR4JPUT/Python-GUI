from PySide6.QtWidgets import QPushButton , QWidget , QGridLayout , QSizePolicy , QLabel , QHBoxLayout , QVBoxLayout , QLineEdit # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        # Create the buttons
        button_1 = QPushButton("Red")
        button_2 = QPushButton("Green")
        button_3 = QPushButton("Blue")
        button_4 = QPushButton("Yellow")
        button_5 = QPushButton("Pink")
        button_6 = QPushButton("Black")
        button_7 = QPushButton("White")
        button_8 = QPushButton("Gray")
        button_9 = QPushButton("Brown")
        button_10 = QPushButton("Purple")
        button_11 = QPushButton("Orange")
        button_12 = QPushButton("Cyan")
        # Set the size policy of the buttons
        button_1.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_2.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_3.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_4.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_5.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_6.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_7.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_8.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_9.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_10.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_11.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        button_12.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)       
        # Create the layout
        layout = QGridLayout()
        layout.addWidget(button_1, 0, 0)
        layout.addWidget(button_2, 0, 1)
        layout.addWidget(button_3, 0, 2)
        layout.addWidget(button_4, 1, 0)
        layout.addWidget(button_5, 1, 1)
        layout.addWidget(button_6, 1, 2)
        layout.addWidget(button_7, 2, 0)
        layout.addWidget(button_8, 2, 1)
        layout.addWidget(button_9, 2, 2)
        layout.addWidget(button_10, 3, 0)
        layout.addWidget(button_11, 3, 1)
        layout.addWidget(button_12, 3, 2)

        self.setLayout(layout)
        