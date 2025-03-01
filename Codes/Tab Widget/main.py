from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QLabel , QPushButton , QHBoxLayout , QLineEdit  # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        #form
        tab_widget = QTabWidget()
        Widget_form = QWidget()
        Label = QLabel("Full Name :")
        LineEdit = QLineEdit()
        form_layout = QHBoxLayout()
        form_layout.addWidget(Label)
        form_layout.addWidget(LineEdit)
        Widget_form.setLayout(form_layout)

        #Buttons
        Widget_Button = QWidget()
        Button = QPushButton("Submit")
        Button.clicked.connect(self.Submit)

        Button2 = QPushButton("Cancel")
        Button2.clicked.connect(self.Cancel)

        Button_layout = QVBoxLayout()
        Button_layout.addWidget(Button)
        Button_layout.addWidget(Button2)
        Widget_Button.setLayout(Button_layout)

        tab_widget.addTab(Widget_form , "Form")
        tab_widget.addTab(Widget_Button , "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)
        self.setLayout(layout)

    def Submit(self):
        print("Submit")

    def Cancel(self):
        print("Cancel")