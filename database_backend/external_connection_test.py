import mysql.connector
import os
from mysql.connector import Error

def connection_test():
    my_host = os.environ.get('DB_WORKER_HOST')
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_user = os.environ.get('DB_USER')
    my_password = os.environ.get('DB_USER_PASSWORD')
    my_path_to_data = os.environ.get('PATH_TO_WORKER_RESULTS')

    file_list = os.listdir(my_path_to_data)
    db_table_name_list = []

    
    try:
        print("Trying to connect to database")
        #Connecting to the database
        myconnection = mysql.connector.connect(host=my_host,
                                        database=my_database,
                                        user=my_user,
                                        password=my_password)
        mycursor = myconnection.cursor()

        #Extracting table names
        mycursor.execute("SHOW TABLES")
        print("List of database tables: {}.".format(mycursor))
        
    except mysql.connector.Error as error:
        print("Failed to connect to database with error {}".format(error))
    


    finally:
        if (myconnection.is_connected()):
            mycursor.close()
            myconnection.close()
            print("MySQL connection is closed")
    return
 