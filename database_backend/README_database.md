# Setting up the MariaDB

Installing MariaDB using apt:
```
sudo apt update && sudo apt upgrade -y && sudo apt install mariadb-server -y
```
Installing mysql.connector (python) *only for workers*
```
sudo locale-gen sv_SE.UTF-8 #This command might be neccesary
sudo pip3 install mysql-connector-python
```

After installation secure the server by following the instructions promted by:
```
sudo mysql_secure_installation
```
### OBS:
* Tutorial for letting other machines connect the server: 
[Remote access tutorial](https://www.cyberciti.biz/tips/how-do-i-enable-remote-access-to-mysql-database-server.html)
* Increasing the log file size so longBlob is accepted:
[Increase log file size](https://support.plesk.com/hc/en-us/articles/115001738733-How-to-change-the-innodb-log-file-size-value-in-MySQL-MariaDB)
* The root password will be the same as for the snic API
* Then login and create users and databases depending on flavor...




## Usefull commands in MySQL:

*Login in*
```
sudo mysql -u root -p #login as root on localhost
mysql -u your_user -h your_host -p #login general case
````

*Commands related to users:*
```
CREATE USER 'database_user'@'localhost' IDENTIFIED BY 'user_password'; #Bad example
CREATE USER IF NOT EXISTS 'database_user'@'localhost' IDENTIFIED BY 'user_password'; #Good example

#List all users:
SELECT user, host FROM mysql.user;

#Alter users:
ALTER USER 'database_user'@'localhost' IDENTIFIED BY 'new_password';
DROP USER 'database_user'@'localhost'; #Bad example
DROP USER IF EXISTS 'database_user'@'localhost'; #Good example
```

*Granting privileges:*
```
#Privileges types:
ALL PRIVILEGES #Grants all privileges to a user account.
CREATE #The user account is allowed to create databases and tables.
DROP #The user account is allowed to drop databases and tables.
DELETE #The user account is allowed to delete rows from a specific table.
INSERT #The user account is allowed to insert rows into a specific table.
SELECT #The user account is allowed to read a database.
UPDATE #The user account is allowed to update table rows.

#Show all permissions for a user:
SHOW GRANTS FOR 'database_user'@'localhost';

#Granting permissions:
GRANT permission1, permission2 ON database_name.table_name TO 'database_user'@'localhost';

#Revoke permissions:
REVOKE ALL PRIVILEGES ON database_name.* TO 'database_user'@'localhost';
```

*Creating and manage tables and databases*
```
CREATE DATABASE database_name; #Worse
CREATE DATABASE IF NOT EXISTS database_name; #Better
DROP DATABASE IF EXISTS database_name;

#List databases and tables
SHOW DATABASES;
SHOW TABLES;

#Use certain database
USE database_name;
```   
