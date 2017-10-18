# To-Do-App-MySQL
Technologies used: Google's Cloud Platform, MySQL/PyMySQL/SQL, Python 

A To-Do App I created with Python and PyMySQL. Application includes a GUI that users can use to create and delete "tasks." These tasks are inserted and removed from a MySQL database hosted on a Google Cloud SQL Instance. Originally used a local MySQL instance.

# Setting up and using the app
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

Make sure that your client machine's IP address (machine on which you cloned the repository) is whitelisted by your MySQL server. If not, the client may not be able to connect to the server. If using a Google Cloud SQL Instance, do this by going to:<br>
<i>Instance Details</i> --> <i>Authorization</i> --> <i>Add Network</i>

Now, run app_driver.py. The application should launch:

![Alt text](images/todo1.PNG?raw=true "Application immediately after launch")

Note that any existing rows (entries) in the <i>tasks</i> table are automatically fetched and displayed.<br><br>


To add a task, first fill in the text fields and select a due date:

![Alt text](images/todo2.PNG?raw=true "Filling in text fields and selecting a due date")

Now, click the <i>Create Task</i> button to add the task to the database!

![Alt text](images/todo3.PNG?raw=true "New task added")

Notice that the task is now visible in the table at the bottom of the window.<br><br>


To remove a task, click on the row number associated with the task. This should highlight the whole row:

![Alt text](images/todo4.PNG?raw=true "Task highlighted")

Now click the <i>Remove Selected Tasks</i> button to remove the highlighted task. You can select and remove more than one task at a time by highlighting multiple rows.

![Alt text](images/todo5.PNG?raw=true "Task removed")

The task(s) have been removed from the database and no are no longer displayed

