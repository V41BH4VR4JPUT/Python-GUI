from PySide6.QtCore import Qt # type: ignore
from PySide6.QtWidgets import QSlider , QApplication  # type: ignore

def slider_moved(value):
    print("Slider Moved : ",value)

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setSingleStep(1)
slider.valueChanged.connect(slider_moved)
slider.show()
app.exec()
