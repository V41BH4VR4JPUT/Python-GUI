from PySide6.QtWidgets import QMainWindow , QToolBar ,QPushButton , QStatusBar # type: ignore
from PySide6.QtCore import QSize # type: ignore
from PySide6.QtGui import QAction , QIcon # type: ignore

class MainWindow(QMainWindow):
    def __init__(self,app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Window")

        Menu = self.menuBar()
        FileMenu = Menu.addMenu("File")
        FileMenu.addAction("New")
        FileMenu.addAction("Open")
        FileMenu.addAction("Save")
        FileMenu.addAction("Save As")

        EditMenu = Menu.addMenu("Edit")
        EditMenu.addAction("Cut")
        EditMenu.addAction("Copy")
        EditMenu.addAction("Paste")

        HelpMenu = Menu.addMenu("Help")
        HelpMenu.addAction("About")
        HelpMenu.addAction("Contact")

        Quit = Menu.addAction("Quit")
        Quit.triggered.connect(self.app.quit)

        toolbar = QToolBar("Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        toolbar.addAction("New")
        toolbar.addAction("Open")
        toolbar.addAction("Save")
        toolbar.addAction("Save As")
        Quit2 = toolbar.addAction("Quit")
        Quit2.triggered.connect(self.app.quit)

        Action = QAction("Edit",self)
        Action.setStatusTip("Editted")
        Action.triggered.connect(self.Workdone)
        toolbar.addAction(Action)

        Action2 = QAction(QIcon("star.png"),"Star",self)
        Action2.setStatusTip("Started")
        Action2.triggered.connect(self.Workdone)
        # Action2.setCheckable(True)
        toolbar.addAction(Action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Button"))

        self.setStatusBar(QStatusBar(self))

        Rock = QPushButton("Rock")
        Rock.clicked.connect(self.Workdone)
        self.setCentralWidget(Rock)

    def Workdone(self):
            self.statusBar().showMessage("Work Done",2000)