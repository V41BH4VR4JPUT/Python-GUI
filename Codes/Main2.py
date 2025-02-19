from PySide6.QtWidgets import QApplication, QWidget # type: ignore
import sys

app = QApplication(sys.argv)
window = QWidget()
window.show()

app.exec()