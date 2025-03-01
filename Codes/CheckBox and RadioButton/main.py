from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QRadioButton, QPushButton, QLabel , QLineEdit, QGroupBox , QButtonGroup # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox and RadioButton")

        os = QGroupBox("Operating System")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.onChecked)
        linux = QCheckBox("Linux")
        linux.toggled.connect(self.onChecked)
        mac = QCheckBox("Mac")
        mac.toggled.connect(self.onChecked)

        #Exclusive Check Box
        drinks = QGroupBox("Drinks")
        coffee = QCheckBox("Coffee")
        tea = QCheckBox("Tea")
        juice = QCheckBox("Juice")
        tea.setChecked(True)

        ExclusiveGroup = QButtonGroup(self)
        ExclusiveGroup.addButton(coffee)
        ExclusiveGroup.addButton(tea)
        ExclusiveGroup.addButton(juice)
        ExclusiveGroup.setExclusive(True)

        answers = QGroupBox("Answers")
        answer1 = QRadioButton("Answer 1")
        answer2 = QRadioButton("Answer 2")
        answer3 = QRadioButton("Answer 3")
        answer2.setChecked(True)

        answersLayout = QVBoxLayout()
        answersLayout.addWidget(answer1)
        answersLayout.addWidget(answer2)
        answersLayout.addWidget(answer3)
        answers.setLayout(answersLayout)

        drinksLayout = QVBoxLayout()
        drinksLayout.addWidget(coffee)
        drinksLayout.addWidget(tea)
        drinksLayout.addWidget(juice)
        drinks.setLayout(drinksLayout)

        osLayout = QVBoxLayout()
        osLayout.addWidget(windows)
        osLayout.addWidget(linux)
        osLayout.addWidget(mac)
        os.setLayout(osLayout)

        Layout = QHBoxLayout()
        Layout.addWidget(os)
        Layout.addWidget(drinks)
      
        vLayout = QVBoxLayout()
        vLayout.addLayout(Layout)
        vLayout.addWidget(answers)
        self.setLayout(vLayout)


    def onChecked(self):
        print("Checked")

       