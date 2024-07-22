from flask import jsonify, request
from mysql.connector import Error
from ..database import connection

class User_model():

    def m_create_user(self, userName, name, lastName, number, email, identification, profile, password):
        try:
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO users (userName, name, lastName, number, email, identification, profileId, userPassword)
                              VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(userName, 
                                                                   name, 
                                                                   lastName, 
                                                                   number, 
                                                                   email, 
                                                                   identification, 
                                                                   profile, 
                                                                   password))

            connection.commit()
            cursor.close()
            return jsonify({"informacion": "ok"})
        except Error as e:
            return jsonify({"informacion": str(e)})