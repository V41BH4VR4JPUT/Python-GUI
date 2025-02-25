from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox # type: ignore

class button(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Custom Button")

        button = QPushButton("Click")
        button.clicked.connect(self.on_click)
        button.pressed.connect(self.on_press)
        button.released.connect(self.on_release)

        layout = QVBoxLayout()
        layout.addWidget(button)
        self.setLayout(layout)

    def on_click(self):
        QMessageBox.information(self, "Information", "Button Clicked")

    def on_press(self):
        QMessageBox.information(self, "Information", "Button Pressed")

    def on_release(self):
        QMessageBox.information(self, "Information", "Button Released")
        