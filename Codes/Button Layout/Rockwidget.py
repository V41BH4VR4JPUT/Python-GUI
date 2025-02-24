from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout # type: ignore

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Set the window title
        self.setWindowTitle("Rock Widget")
        # Set the window size
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Add a button to the window
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)
        # Add a button to the window
        rock_button = QPushButton("Rock")
        button_layout.addWidget(rock_button)
        rock_button.clicked.connect(self.Rock)
        # Add a button to the window
        paper_button = QPushButton("Paper")
        button_layout.addWidget(paper_button)
        paper_button.clicked.connect(self.Paper)
        # Add a button to the window
        scissors_button = QPushButton("Scissors")
        button_layout.addWidget(scissors_button)
        scissors_button.clicked.connect(self.Scissors)
        # Add a button to the window
        Quit_button = QPushButton("Quit")
        layout.addWidget(Quit_button)
        Quit_button.clicked.connect(self.Quit)
        
    
    def Rock(self):
        print("Rock")
        
    def Paper(self):
        print("Paper")
        
    def Scissors(self):
        print("Scissors")
    
    def Quit(self):
        print("Quit")
        self.close()