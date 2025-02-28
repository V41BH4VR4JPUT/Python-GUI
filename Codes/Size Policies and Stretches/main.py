from PySide6.QtWidgets import QWidget , QVBoxLayout, QLabel, QSizePolicy, QPushButton , QHBoxLayout , QLineEdit # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Size Policies and Stretches")

        label = QLabel("Text :")
        line_Edit = QLineEdit()
        #Expanding size policy is used to make the widget take as much space as possible
        line_Edit.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Fixed)

        H_Layout = QHBoxLayout()
        H_Layout.addWidget(label)
        H_Layout.addWidget(line_Edit)

        Button_1 = QPushButton("Button 1")
        Button_2 = QPushButton("Button 2")
        Button_3 = QPushButton("Button 3")

        h_Layout = QHBoxLayout()
        #Stretch factor is used to determine how much space a widget will take compared to other widgets
        h_Layout.addWidget(Button_1 , 2)# Button 1 will take twice the space of Button 2 and Button 3
        h_Layout.addWidget(Button_2 , 1)# Button 2 will take half the space of Button 1 and Button 3
        h_Layout.addWidget(Button_3 , 1)# Button 3 will take half the space of Button 1 and Button 2

        v_Layout = QVBoxLayout()
        v_Layout.addLayout(H_Layout)
        v_Layout.addLayout(h_Layout)

        self.setLayout(v_Layout)