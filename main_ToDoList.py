import sys
import json
import PyQt5

from PyQt5.QtCore import QSize, Qt, QAbstractListModel
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout,QHBoxLayout, QLineEdit, QListView
from PyQt5.QtGui import QColor, QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ToDo List")

# Main application loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Windows")
    window = MainWindow()
    window.show()
    sys.exit( app.exec_() )
