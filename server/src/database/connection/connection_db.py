import mysql.connector
from mysql.connector import Error

def mysql_connect_db(app):

    try:
        
        connection = mysql.connector.connect(

            MYSQL_USER = app.config['MYSQL_USER'],
            MYSQL_HOST = app.config['MYSQL_HOST'],
            MYSQL_PASSWORD = app.config['MYSQL_PASSWORD'],
            MYSQL_DB =  app.config['MYSQL_DB']  

        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)