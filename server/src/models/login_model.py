from flask import jsonify, request
from mysql.connector import Error
from ..database import Connector

db = Connector()

class Login_model():

    def m_check_user_authentication(self, userName, email):
        try:
            cursor = db.connection.cursor()
            cursor.execute("""SELECT * from users WHERE userName = %s and email = %s""",(userName, email))
            data = cursor.fetchone()
            cursor.close()
            return data
        except Error as e: 
            return e

    def get_role(role_id):

        try:
            cursor = db.connection.cursor(dictionary=True)
            cursor.execute("SELECT roleProfile FROM profiles_roles WHERE id = %s", (role_id,))
            role = cursor.fetchone()
            cursor.close()
            return role['roleProfile'] if role else None
        except Error as e: 
            return e