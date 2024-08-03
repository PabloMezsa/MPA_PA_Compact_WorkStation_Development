from flask import jsonify, request
from mysql.connector import Error
from ..database import Connector
from .include.getAllUser import All_users

db = Connector()

class User_model():

    def m_consult_users(self):
        try:
            cursor = db.connection.cursor()
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
            cursor = db.connection.cursor()
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

    def m_create_user(self, username, email, profile, password):
        try:
            cursor = db.connection.cursor()
            cursor.execute("""INSERT INTO users (username, email, profileId, password)
                              VALUES (%s,%s,%s,%s)""",(username, email, profile, password))
            db.connection.commit()
            cursor.close()
            return jsonify({"Information": "Ok"}), 201
        except Error as e:
            return jsonify({"Information": str(e)}), 500
    
    def m_uptade_user(self, username, email, profile, password):
    
        try: 
            cursor = db.connection.cursor()
            cursor.execute("""UPDATE users SET username = %s, email = %s, profileId = %s, 
                              password = %s""",(username, email, profile, password))
            db.connection.commit()
            cursor.close()
            return ({"Message":"User Has been Updated"}), 201

        except Error as e:
                return jsonify({"Information": str(e)}), 500
    
    def m_delete_user(self, _id):

        try:
            cursor = db.connection.cursor()
            cursor.execute("""DELETE FROM users WHERE id = %s""",(_id,))
            db.connection.commit()
            cursor.close()
            return ({"Message":"User Deleted"}), 201
        except Error as e:
            return jsonify({"Information": str(e)}), 500  