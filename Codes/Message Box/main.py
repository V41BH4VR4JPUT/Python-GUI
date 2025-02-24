from PySide6.QtWidgets import QWidget , QPushButton , QVBoxLayout , QMessageBox # type: ignore

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Box")

        Button_Hard = QPushButton("Hard")
        Button_Hard.clicked.connect(self.Hard)

        Button_About = QPushButton("About")
        Button_About.clicked.connect(self.About)

        Button_Critical = QPushButton("Critical")
        Button_Critical.clicked.connect(self.Critical)

        Button_Question = QPushButton("Question")
        Button_Question.clicked.connect(self.Question)

        Button_warning = QPushButton("Warning")
        Button_warning.clicked.connect(self.Warning)

        Button_information = QPushButton("Information")
        Button_information.clicked.connect(self.Information)

        layout = QVBoxLayout()
        layout.addWidget(Button_Hard)
        layout.addWidget(Button_About)
        layout.addWidget(Button_Critical)
        layout.addWidget(Button_Question)
        layout.addWidget(Button_warning)
        layout.addWidget(Button_information)
        self.setLayout(layout)

    def Hard(self):
        message = QMessageBox()
        message.setMinimumSize(500,500)
        message.setWindowTitle("Hard")
        message.setText("Some text")
        message.setInformativeText("Some informative text")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)
        # show the message box
        ret = message.exec()
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    
    def About(self):
        ret = QMessageBox.about(self, "About", "Some text")
        print(ret)
        
    
    def Critical(self):
        print("Critical")

    def Question(self):
       
        ret = QMessageBox.question(self, "Question", "Some text", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            print("Yes")
        else:
            print("No")

    def Warning(self):
        ret = QMessageBox.warning(self, "Warning", "Some text", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def Information(self):
        ret = QMessageBox.information(self, "Information", "Some text", QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

