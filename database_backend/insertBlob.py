import mysql.connector
import os
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insert_db_table(tableName):
    my_host = os.environ.get('DB_WORKER_HOST')
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_user = os.environ.get('DB_USER')
    my_password = os.environ.get('DB_USER_PASSWORD')
    my_path_to_data = os.environ.get('PATH_TO_WORKER_RESULTS')

    print("Inserting new table name {} into database {}.".format(tableName,my_database))
        try:
            mydb = mysql.connector.connect(host=my_host,
                                            database=my_database,
                                            user=my_user,
                                            password=my_password)
            mycursor = mydb.cursor()
            mycursor.execute("CREATE TABLE `tableName` (name VARCHAR(255), file_blob LONGBLOB)")

        except mysql.connector.Error as error:
            print("Failed to create table database {} with error {}".format(my_database, error))




def insertResult(tableName, fileBlobName , pathToFile):
    my_host = os.environ.get('DB_WORKER_HOST')
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_user = os.environ.get('DB_USER')
    my_password = os.environ.get('DB_USER_PASSWORD')

    print("Inserting BLOB into table {}.".format(tableName))
    try:
        connection = mysql.connector.connect(host=my_host,
                                             database=my_database,
                                             user=my_user,
                                             password=my_password)


        cursor = connection.cursor()
        sql_insert_blob_query = "INSERT INTO `tableName` (`resultFilename`, `my_fileBlob`)  VALUES (%s, %s)"

        my_fileBlob = convertToBinaryData(str(pathToFile+fileBlobName))

        # Convert data into tuple format
        insert_blob_tuple = (resultFilename, my_fileBlob)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Successfully inserted BLOB into MySQL table {}".format(tableName))

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {} with {}".format(tableName, error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return


def insertingAllResults(xmlFileName):
    my_host = os.environ.get('DB_WORKER_HOST')
    my_database = os.environ.get('DB_DATABASE_NAME')
    my_user = os.environ.get('DB_USER')
    my_password = os.environ.get('DB_USER_PASSWORD')
    my_path_to_data = os.environ.get('PATH_TO_WORKER_RESULTS')

    file_list = os.listdir(my_path_to_data)
    db_table_name_list = []

    #inserting all the values
    for filename in file_list:
        print("Inserting BLOBS into table {} BLOB into table {}.".format(tableName))
        try:
            mydb = mysql.connector.connect(host=my_host,
                                            database=my_database,
                                            user=my_user,
                                            password=my_password)
            mycursor = mydb.cursor()
            mycursor.execute("SHOW TABLES")
            
            for table in mycursor:
                db_table_name_list.append(table)

        except mysql.connector.Error as error:
            print("Failed to get table names in database {} with error {}".format(my_database, error))

    if xmlFileName in db_table_name_list:
       return print("There is already a result for msh file: {}".format(xmlFileName))
    else:
        insert_db_table(xmlFileName)
        for result_file_name in file_list:
            insertResult(xmlFileName, result_file_name, my_path_to_data)
            return print("{} result files are inserted into database."format(my_database))

if __name__ == "__main__":
    insertingAllResults("r1a0.xml")
