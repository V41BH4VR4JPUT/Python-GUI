from PySide6.QtWidgets import QMainWindow, QApplication # type: ignore
import sys
from Main import MainWindow

app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
app.exec()