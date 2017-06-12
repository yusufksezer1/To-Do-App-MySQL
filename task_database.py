import pymysql

class TaskDatabase():

    def __init__(self):
        # establish connection to database
        self.db = pymysql.connect("localhost", "username", "password", "database_name")
        self.cursor = self.db.cursor()

    def get_tasks(self):
        self.cursor.execute("SELECT * FROM tasks ORDER BY dueDate ASC")
        return self.cursor.fetchall()

    def insert_new_task(self, name, description, date):
        query = "INSERT INTO tasks (name, description, dueDate) VALUES ('%s', '%s', '%s')" % (name, description, date)
        self.cursor.execute(query)
        self.db.commit()

    def get_column_names(self):
        query = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='todoapp' AND `TABLE_NAME`='tasks'"
        self.cursor.execute(query)
        tpl = self.cursor.fetchall()
        print(tpl)
        lst = [elem[0] for elem in tpl]
        return lst

    def delete_task(self, name, description, date):
        query = "DELETE FROM tasks WHERE name='%s' AND description='%s'" % (name, description)
        self.cursor.execute(query)
        self.db.commit()