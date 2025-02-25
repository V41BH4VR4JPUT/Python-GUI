from PySide6.QtWidgets import QApplication # type: ignore
from main import button
import sys

app = QApplication(sys.argv)
window = button()
window.show()
app.exec()