import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='felix_root', password = '1234')

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for i in mycursor:
	print(i)