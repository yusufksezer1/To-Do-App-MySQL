# To-Do-App-MySQL
Technologies used: Google's Cloud Platform, MySQL/PyMySQL/SQL, Python 

A To-Do App I created with Python and PyMySQL. Application includes a GUI that users can use to create and delete "tasks." These tasks are inserted and removed from a MySQL database hosted on a Google Cloud SQL Instance. Originally used a local MySQL instance.

# Using the app
First create a local or remote MySQL database. Create a file named credentials.py and insert the following code:
SERVER_IP = "your ip here"
USERNAME = "your MySQL instance username"
PASSWORD = "your MySQL instance password"
DATABASE_NAME = "name of database"
