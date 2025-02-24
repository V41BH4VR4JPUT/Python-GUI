from PySide6.QtWidgets import QApplication # type: ignore
from main import Widget
import sys

app = QApplication(sys.argv)
window = Widget()
window.show()
app.exec()