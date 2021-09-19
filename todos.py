from PyQt5.QtCore import Qt, QAbstractListModel
from PyQt5.QtGui import QColor



class ToDosModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def rowCount(self, index):
        return len(self.todos)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return QColor("green")
            else:
                return QColor("red")

    def delete_todo(self, indexes):
        index = indexes[0]
        row = index.row()
        del self.todos[row]
        self.layoutChanged.emit()

    def add_todo(self, text):
        self.todos.append( (False, text) )
        self.layoutChanged.emit()

    def complete_todo(self, indexes):
        index = indexes[0]
        row = index.row()
        status, text = self.todos[row]
        self.todos[row] = (not status, text)
        self.dataChanged.emit(index, index)
