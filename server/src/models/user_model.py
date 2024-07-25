from flask import jsonify, request
from mysql.connector import Error
from ..database import connection
from .include.getAllUser import All_users

class User_model():

    def m_consult_users(self):
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT * FROM users""")
            data = cursor.fetchall()
            cursor.close()
            users = [All_users.db_user_info(row) for row in data]
            users_json = [All_users.get_user_data(user) for user in users]
            return users_json
        except Error as e:
            return e

    def m_consult_user_id(self, _id):
        try:
            cursor = connection.cursor()
            cursor.execute("""SELECT * from users WHERE id = %s""",(_id,))
            data = cursor.fetchone()
            cursor.close()
            user = All_users.db_user_info(data)
            users_json = All_users.get_user_data(user)
            return users_json
        except Error as e: 
            return e
        except Exception:
            return None

    def m_create_user(self, userName, name, lastName, number, email, identification, profile, password):
        try:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users (userName, name, lastName, number, email, identification, profileId, userPassword)
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(userName, name, lastName, number, email, identification, profile, password))
            connection.commit()
            cursor.close()
            return jsonify({"Information": "Ok"}), 201
        except Error as e:
            return jsonify({"Information": str(e)}), 500
    
    def m_uptade_user(self, userName, name, lastName, number, email, identification, profile, password):
    
        try: 
            cursor = connection.cursor()
            cursor.execute("""UPDATE users SET userName = %s, name = %s, lastName = %s, number = %s, email = %s, identification = %s, 
                      profileId = %s, userPassword = %s""",(userName, name, lastName, number, email, identification, profile, password))
            connection.commit()
            cursor.close()
            return ({"Message":"User Has been Updated"}), 201

        except Error as e:
                return jsonify({"Information": str(e)}), 500
    
    def m_delete_user(Sself, _id):

        try:
            cursor = connection.cursor()
            cursor.execute("""DELETE FROM users WHERE id = %s""",(_id,))
            connection.commit()
            cursor.close()
            return ({"Message":"User Deleted"}), 201
        except Error as e:
            return jsonify({"Information": str(e)}), 500  