# To-Do-App-MySQL
Technologies used: Google's Cloud Platform, MySQL/PyMySQL/SQL, Python 

A To-Do App I created with Python and PyMySQL. Application includes a GUI that users can use to create and delete "tasks." These tasks are inserted and removed from a MySQL database hosted on a Google Cloud SQL Instance. Originally used a local MySQL instance.

# Using the app
First create a local or remote MySQL database. Create a file named credentials.py and insert the following code:<br>

<i>
SERVER_IP = "localhost or ip of remote server"<br>
USERNAME = "your MySQL instance username"<br>
PASSWORD = "your MySQL instance password"<br>
DATABASE_NAME = "name of database"<br>
</i><br>

The server should contain a Schema named <i>ToDoApp</i>. The <i>ToDoApp</i> schema should contain a <i>tasks</i> table with the columns <i>name</i>, <i>description</i>, and <i>dueDate</i> of types <i>VARCHAR(50)</i>, <i>VARCHAR(350)</i>, and <i>DATE</i> respectively. Here is a snapshot of how to set this up in MySQL Workbench:

