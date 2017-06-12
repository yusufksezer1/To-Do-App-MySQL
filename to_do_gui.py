from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit, QTableView, QHeaderView)
from PyQt5.QtGui import (QStandardItemModel, QStandardItem)
from PyQt5.QtCore import (QDate)

class ToDoWindow(QWidget):

    def __init__(self, db_accessor):
        super().__init__()
        self.db_accessor = db_accessor # database delegate
        self.init_ui()

    def init_ui(self):
        self.hBox = QHBoxLayout()
        self.hBox2 = QHBoxLayout()
        self.vBox = QVBoxLayout()

        self.removeBtn = QPushButton()
        self.removeBtn.setText("Remove Selected Tasks")
        self.removeBtn.clicked[bool].connect(self.remove_task)

        self.createBtn = QPushButton()
        self.createBtn.setText("Create Task")
        self.createBtn.setFixedSize(200, 50)
        self.createBtn.clicked[bool].connect(self.create_task)

        self.nameBox = QLineEdit()
        self.nameBox.setPlaceholderText("Task Name")
        self.nameBox.setMaxLength(50)
        self.nameBox.setFixedSize(1185, 50)

        self.descBox = QTextEdit()
        self.descBox.setPlaceholderText("Task Description")
        self.descBox.setFixedSize(600, 500)

        self.calendar = QCalendarWidget()
        self.calendar.setFixedSize(775, 500)

        self.table = QTableView()
        self.table.setFixedSize(1400, 400)

        # stretch columns to fill table's width and load data from database into table
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.update_task_view(self.db_accessor.get_tasks())

        # add widgets to appropriate horizontal layouts
        self.hBox.addWidget(self.createBtn)
        self.hBox.addWidget(self.nameBox)
        self.hBox2.addWidget(self.descBox)
        self.hBox2.addWidget(self.calendar)

        # add horizontal layouts to vertical layout
        # add remove button and table to vertical layout
        self.vBox.addLayout(self.hBox)
        self.vBox.addLayout(self.hBox2)
        self.vBox.addWidget(self.removeBtn)
        self.vBox.addWidget(self.table)

        # Create and display window
        self.setLayout(self.vBox)
        self.setWindowTitle('To-Do')
        self.show()

    # insert a new task into the database and refresh table to reflect insertion
    def create_task(self):
        name = self.nameBox.text().replace("'", "\\'")
        description = self.descBox.toPlainText().replace("'", "\\'")
        date = self.calendar.selectedDate().toString("yyyy-MM-dd")
        self.db_accessor.insert_new_task(name, description, date)
        self.update_task_view(self.db_accessor.get_tasks())

    # refresh table
    def update_task_view(self, result_set):
        model = QStandardItemModel()
        list_of_entries = [list(map(str, elem)) for elem in result_set]
        model.setHorizontalHeaderLabels(self.db_accessor.get_column_names())
        res_rows = list_of_entries
        for row in res_rows:
            model.appendRow(self.get_items_row(row))
        self.table.setModel(model)
        self.table.resizeRowsToContents()
        self.nameBox.setText("")
        self.descBox.setText("")
        self.calendar.setSelectedDate(QDate.currentDate())

    # set the values from the result set into a new row in the model format
    def get_items_row(self, result_row):
        item_row = []
        for val in result_row:
            item = QStandardItem(val)
            item.setEditable(False)
            item_row.append(item)
        return item_row

    def remove_task(self):
        model = self.table.model()

        # get the indeces of the currently selected rows
        indices = [elem.row() for elem in self.table.selectionModel().selectedRows()]

        # remove the tasks from the database and refresh table to reflect deletion
        for index in indices:
            name = model.data(model.index(index, 0)).replace("'", "\\'")
            description = model.data(model.index(index, 1)).replace("'", "\\'")
            date = model.data(model.index(index, 2))
            self.db_accessor.delete_task(name, description, date)

        self.update_task_view(self.db_accessor.get_tasks())