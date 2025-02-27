from PySide6.QtWidgets import QTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("QTextEdit")

        self.text_edit = QTextEdit()
        # self.text_edit.textChanged.connect(self.text_changed)

        #buttons
        Current_text_button = QPushButton("Current Text")
        Current_text_button.clicked.connect(self.current_text)

        Copy_button = QPushButton("Copy")
        Copy_button.clicked.connect(self.text_edit.copy)

        Cut_button = QPushButton("Cut")
        Cut_button.clicked.connect(self.text_edit.cut)

        Paste_button = QPushButton("Paste")
        # Paste_button.clicked.connect(self.text_edit.paste)

        Undo_button = QPushButton("Undo")
        Undo_button.clicked.connect(self.text_edit.undo)

        Redo_button = QPushButton("Redo")
        Redo_button.clicked.connect(self.text_edit.redo)

        Set_plain_text_button = QPushButton("Set Plain Text")
        Set_plain_text_button.clicked.connect(self.setPlainText)

        Set_html_button = QPushButton("Set HTML")
        Set_html_button.clicked.connect(self.setHtml)

        Clear_button = QPushButton("Clear")
        Clear_button.clicked.connect(self.text_edit.clear)

        #Layouts
        H_layout = QHBoxLayout()
        H_layout.addWidget(Copy_button)
        H_layout.addWidget(Cut_button)
        H_layout.addWidget(Paste_button)
        H_layout.addWidget(Undo_button)
        H_layout.addWidget(Redo_button)
        H_layout.addWidget(Set_plain_text_button)
        H_layout.addWidget(Set_html_button)
        H_layout.addWidget(Clear_button)
        H_layout.addWidget(Current_text_button)

        V_layout = QVBoxLayout()
        V_layout.addLayout(H_layout)
        V_layout.addWidget(self.text_edit)

        self.setLayout(V_layout)

    def current_text(self):     
        print(self.text_edit.toPlainText())

    def setPlainText(self):
        self.text_edit.setPlainText("Support for this channel comes from our friends at Scrimba – the coding platform that's reinvented interactive learning")
    
    def setHtml(self):
        self.text_edit.setHtml("<h1>Support for this channel comes from our friends at Scrimba – the coding platform that's reinvented interactive learning</h1>")