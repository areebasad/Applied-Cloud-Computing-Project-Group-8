import mysql.connector
import os
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    file.close()
    return binaryData


def insert_db_table(tableName, cursor):
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_path_to_data = os.environ.get('PATH_TO_WORKER_RESULTS')

    print("Trying to insert new table name {} into database {}.".format(tableName,my_database))
    try:

        insert_table_query = "CREATE TABLE "+str(tableName)+" (file_name VARCHAR(255), file_blob LONGBLOB)"
        cursor.execute(insert_table_query)
        print("Successfully inserted table {} into database {}".format(tableName, my_database))

    except mysql.connector.Error as error:
        print("Failed to create table {} in database {} with error {}".format(tableName, my_database, error))

    return




def insertResult(connection, cursor, tableName, fileBlobFullName , pathToFile):
    print("Inserting BLOB into table {}.".format(tableName))
    try:
        sql_insert_blob_query = "INSERT INTO "+str(tableName)+ " (`file_name`, `file_blob`)  VALUES (%s, %s)"

        my_fileBlob = convertToBinaryData(str(pathToFile+fileBlobFullName))
        my_fileBlobName, separator, extension = fileBlobFullName.partition(".")

        # Convert data into tuple format
        insert_blob_tuple = (my_fileBlobName, my_fileBlob)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Successfully inserted {}-blob into MySQL table {}".format(fileBlobFullName, tableName))

    except mysql.connector.Error as error:
        print("Failed inserting {}-blob data into MySQL table {} with {}".format(fileBlobFullName, tableName, error))

    return


def insertingAllResults(xmlFileFullName):
    my_host = os.environ.get('DB_WORKER_HOST')
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_user = os.environ.get('DB_USER')
    my_password = os.environ.get('DB_USER_PASSWORD')
    my_path_to_data = os.environ.get('PATH_TO_WORKER_RESULTS')

    file_list = os.listdir(my_path_to_data)
    db_table_name_list = []

    xmlFileName, separator, xmlFileEextension = xmlFileFullName.partition(".")

    #inserting all the values
    print("Trying to inserting all related file BLOBS into table: {}.".format(xmlFileName))
    for filename in file_list:
        try:
            myconnection = mysql.connector.connect(host=my_host,
                                            database=my_database,
                                            user=my_user,
                                            password=my_password)
            mycursor = myconnection.cursor()
            mycursor.execute("SHOW TABLES")
            
            for table in mycursor:
                db_table_name_list.append(table)

            if xmlFileName in db_table_name_list:
                return print("ERROR NOT APPENDING VALUES - There is already a result for msh file: {}".format(xmlFileName))
            else:
                insert_db_table(xmlFileName, mycursor)
                
                for result_file_name in file_list:
                    insertResult(myconnection, mycursor, xmlFileName, result_file_name, my_path_to_data)

                print("Successfully inserted all files for msh file {} into table {} in database {}.".format(xmlFileFullName, xmlFileName, my_database))
        
        except mysql.connector.Error as error:
            print("Failed to connect to database with error {}".format(error))


        finally:
            if (myconnection.is_connected()):
                    mycursor.close()
                    myconnection.close()
                    print("MySQL connection is closed")
    return 


  

if __name__ == "__main__":
    insertingAllResults("r1a0")
