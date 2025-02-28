from PySide6.QtWidgets import QApplication # type: ignore
from main import Screen
import sys

app = QApplication(sys.argv)
screen = Screen()
screen.show()
app.exec()
