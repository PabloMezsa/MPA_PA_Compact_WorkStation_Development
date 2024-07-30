import mysql.connector
from mysql.connector import Error
from decouple import config


class Connector():

    def __init__(self):

            self.connection = self.__db_connector()

    def __db_connector(self):

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
                
            return connection

        except Error as e:

            print("Error while connecting to MySQL", e)

            return None