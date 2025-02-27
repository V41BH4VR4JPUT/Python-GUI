from PySide6.QtWidgets import QApplication  # type: ignore
import sys
from main import Screen 

app = QApplication(sys.argv)
window = Screen()
window.show()
app.exec()