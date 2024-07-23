from flask import jsonify, request
from mysql.connector import Error
from ..database import connection
from .include.getAllUser import All_users

class User_model():

    def m_consult_users(self):
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            cursor.close()
            users = [All_users.db_user_info(row) for row in data]
            users_json = [All_users.get_user_data(user) for user in users]
            return jsonify(users_json)
        except Error as e:
            return jsonify({"informacion": str(e)})

    def m_create_user(self, userName, name, lastName, number, email, identification, profile, password):
        try:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users (userName, name, lastName, number, email, identification, profileId, userPassword)
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(userName, name, lastName, number, email, identification, profile, password))
            connection.commit()
            cursor.close()
            return jsonify({"Information": "Ok"})
        except Error as e:
            return jsonify({"Information": str(e)})