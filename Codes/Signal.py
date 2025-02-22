from PySide6.QtWidgets import QPushButton , QApplication , QMainWindow # type: ignore

def button_clicked(data):
    print("Button Clicked : ",data)

app = QApplication()
button = QPushButton("Click Me")
button.setCheckable(True)
button.clicked.connect(button_clicked)
button.show()
app.exec()
# The button_clicked function is called when the button is clicked.
# This is because the clicked signal of the QPushButton is connected to the button_clicked function.
# The button_clicked function is called with no arguments when the button is clicked.
