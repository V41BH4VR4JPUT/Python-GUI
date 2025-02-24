from PySide6.QtWidgets import QApplication, QWidget # type: ignore
import sys

from Rockwidget import RockWidget

app = QApplication(sys.argv)
window = RockWidget()
window.show()
app.exec()