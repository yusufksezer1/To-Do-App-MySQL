import sys
from to_do_gui import ToDoWindow
from PyQt5.QtWidgets import QApplication
from task_database import TaskDatabase

# driver for To-Do app
database = TaskDatabase()
app = QApplication(sys.argv)
window = ToDoWindow(database)
sys.exit(app.exec_())

