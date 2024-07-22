import mysql.connector
from mysql.connector import Error
from decouple import config

try:      
    connection = mysql.connector.connect(

        user = config('MYSQL_USER'),
        host = config('MYSQL_HOST'),
        password = config('MYSQL_PASSWORD'),
        database =  config('MYSQL_DB')  

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