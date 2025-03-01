from PySide6.QtWidgets import QWidget , QComboBox , QPushButton , QVBoxLayout , QHBoxLayout , QLabel # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo Box")

        self.combo = QComboBox(self)
        self.combo.addItem("Python")
        self.combo.addItem("Java")
        self.combo.addItem("C++")
        self.combo.addItem("C#")
        self.combo.addItem("Ruby")
        self.combo.addItem("PHP")
        self.combo.addItem("JavaScript")
        self.combo.addItem("HTML")

        button_current_value = QPushButton("Current Value")
        button_current_value.clicked.connect(self.current_value)
        button_set_Current = QPushButton("Set Current Value")
        button_set_Current.clicked.connect(self.set_current_value)
        button_Get_value = QPushButton("Get Value")
        button_Get_value.clicked.connect(self.get_value)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(button_current_value)
        layout.addWidget(button_set_Current)
        layout.addWidget(button_Get_value)

        self.setLayout(layout)
    
    def current_value(self):
        print(self.combo.currentText())

    def set_current_value(self):
        self.combo.setCurrentText("Python")

    def get_value(self):
        for i in range(self.combo.count()):
            print("Index: ",i," Value: ",self.combo.itemText(i))
       

        