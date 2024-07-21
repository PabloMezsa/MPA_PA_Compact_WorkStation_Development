import mysql.connector
from mysql.connector import Error

def mysql_connect_db(app):

    try:
        
        connection = mysql.connector.connect(

            user = app.config['MYSQL_USER'],
            host = app.config['MYSQL_HOST'],
            password = app.config['MYSQL_PASSWORD'],
            database =  app.config['MYSQL_DB']  

        )

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)