import sys
import json

from PyQt5.QtCore import QSize, Qt, QAbstractListModel
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QListView
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDo List")
        self.setFixedSize(QSize(300,400))

        # Layouts
        layout_main = QVBoxLayout()
        layout_delete_complete = QHBoxLayout()

        # Create widgets
        self.view_list_todo = QListView()
        self.button_delete = QPushButton("Delete ToDo")
        self.button_complete = QPushButton("Mark as Complete")
        self.edit_todo = QLineEdit()
        self.edit_todo.setPlaceholderText("Enter ToDo Description")
        self.button_add = QPushButton("Add ToDo")

        # Add widgets to layouts
        layout_main.addWidget(self.view_list_todo)
        layout_delete_complete.addWidget(self.button_delete)
        layout_delete_complete.addWidget(self.button_complete)
        layout_main.addLayout(layout_delete_complete)
        layout_main.addWidget(self.edit_todo)
        layout_main.addWidget(self.button_add)

        layout_main.setContentsMargins(20,20,20,20)
        layout_main.setSpacing(10)

        # Set up main container widget
        widget_main = QWidget()
        widget_main.setLayout(layout_main)
        self.setCentralWidget(widget_main)



# Main application loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit( app.exec_() )
