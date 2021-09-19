import sys

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow

from todos import ToDosModel

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi('uis/mainwindow.ui', self)

        # Signals / slots
        self.button_delete.clicked.connect(self.on_delete)
        self.button_add.clicked.connect(self.on_add)
        self.button_complete.clicked.connect(self.on_complete)

        # Connect models and views
        initial_todos = [[False, "Take out trash"],[True, "Pay bills"]]
        self.model_todos = ToDosModel(initial_todos)
        self.view_list_todos.setModel(self.model_todos)

    def on_delete(self):
        indexes = self.view_list_todos.selectedIndexes()
        if indexes:
            self.model_todos.delete_todo(indexes)
            self.view_list_todos.clearSelection()

    def on_add(self):
        text = self.edit_todo.text()
        text = text.strip()
        if text:
            self.model_todos.add_todo(text)
            self.edit_todo.setText("")

    def on_complete(self):
        indexes = self.view_list_todos.selectedIndexes()
        if indexes:
            self.model_todos.complete_todo(indexes)
            self.view_list_todos.clearSelection()


# Main application loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit( app.exec_() )
