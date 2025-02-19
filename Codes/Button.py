from PySide6.QtWidgets import QPushButton , QApplication , QMainWindow
import sys

class Button(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button")
        self.button = QPushButton("Click Me")
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
window = Button()
window.show()
app.exec()
