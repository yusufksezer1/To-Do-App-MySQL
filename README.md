# To-Do-App-MySQL
Technologies used: Google's Cloud Platform, MySQL/PyMySQL/SQL, Python 

A To-Do App I created with Python and PyMySQL. Application includes a GUI that users can use to create and delete "tasks." These tasks are inserted and removed from a MySQL database hosted on a Google Cloud SQL Instance. Originally used a local MySQL instance.

# Setting up the app
First, clone this repository into a directory of your choosing.
Now create a local or remote MySQL database. Create a file named credentials.py inside the cloned repository and insert the following lines:<br>

<i>
SERVER_IP = "localhost or ip of remote server"<br>
USERNAME = "your MySQL server username"<br>
PASSWORD = "your MySQL server password"<br>
DATABASE_NAME = "ToDoApp"<br>
</i><br>

The server should contain a Schema named <i>ToDoApp</i>. The <i>ToDoApp</i> schema should contain a <i>tasks</i> table with the columns <i>name</i>, <i>description</i>, and <i>dueDate</i> of types <i>VARCHAR(50)</i>, <i>VARCHAR(350)</i>, and <i>DATE</i> respectively. Here is a snapshot of how to set this up in MySQL Workbench:

![Alt text](images/workbench.PNG?raw=true "Setting up database via MySQL Workbench")

Make sure that your client (machine on which you cloned the repository) is whitelisted by your MySQL server. If not, the client may not be able to connect to the server. If using a Google Cloud SQL Instances, do this by going to:<br>
<i>Instance Details</i> --> <i>Authorization</i> --> <i>Add Network</i>

