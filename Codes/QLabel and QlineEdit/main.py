from PySide6.QtWidgets import QPushButton, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout, QWidget  # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Enter your name:")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.Cursor_position_changed)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Submit")
        button.clicked.connect(self.Button_clicked)
        self.text_Holder_label = QLabel(" Work Done")

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.line_edit)

        layout2 = QVBoxLayout()
        layout2.addLayout(layout)
        layout2.addWidget(button)
        layout2.addWidget(self.text_Holder_label)

        self.setLayout(layout2)

    def Button_clicked(self):
        # print("Full Name: ", self.line_edit.text())
        self.text_Holder_label.setText(self.line_edit.text())

    def text_changed(self):
        self.text_Holder_label.setText(self.line_edit.text())
        # print("Text Changed: ", self.line_edit.text())

    def Cursor_position_changed(self,old,new):
        print("Old: ", old, " New: ", new)

    def editing_finished(self):
        print("Editing Finished")
    
    def return_pressed(self):
        print("Return Pressed")

    def selection_changed(self):
        print("Selection Changed: ", self.line_edit.selectedText())
    
    def text_edited(self , newText):
        print("Text Edited: ", newText)