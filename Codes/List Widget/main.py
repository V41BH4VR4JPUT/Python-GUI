from PySide6.QtWidgets import QHBoxLayout,QAbstractItemView, QCheckBox, QPushButton, QListWidget, QListWidgetItem, QVBoxLayout, QWidget  # type: ignore

class Screen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("List Widget")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"])
        self.list_widget.addItem("Item 6")
        self.list_widget.currentTextChanged.connect(self.on_current_text_changed)
        self.list_widget.currentItemChanged.connect(self.on_current_item_changed)

        add_button = QPushButton("Add Item")
        add_button.clicked.connect(lambda: self.list_widget.addItem("New Item"))

        remove_button = QPushButton("Remove Item")
        remove_button.clicked.connect(lambda: self.list_widget.takeItem(self.list_widget.currentRow()))

        item_Count_button = QPushButton("Item Count")
        item_Count_button.clicked.connect(lambda: print(f"Item Count: {self.list_widget.count()}"))

        Selected_Item_button = QPushButton("Selected Item")
        Selected_Item_button.clicked.connect(lambda: print(f"Selected Item: {self.list_widget.currentItem().text()}"))

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(lambda: self.list_widget.clear())

        H_layout = QVBoxLayout()
        H_layout.addWidget(add_button)
        H_layout.addWidget(remove_button)
        H_layout.addWidget(item_Count_button)
        H_layout.addWidget(Selected_Item_button)
        H_layout.addWidget(clear_button)

        V_layout = QVBoxLayout()
        V_layout.addWidget(self.list_widget)
        V_layout.addLayout(H_layout)

        self.setLayout(V_layout)

    def on_current_text_changed(self, text):
        print(f"Current Text Changed: {text}")

    def on_current_item_changed(self, item):
        print(f"Current Item Changed: {item.text()}")