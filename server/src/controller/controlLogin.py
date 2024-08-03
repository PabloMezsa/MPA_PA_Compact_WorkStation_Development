from flask import jsonify
from ..models import User_login, Login_model
from .sessions import rolUser

class Login_controller():

    def con_authenticate_user(self, info):

        query = User_login.build_user_info(info)
        check = query.authenticate()

        if check is not None and not isinstance(check,BaseException):
            
            if check[1] == info['username']:

                auth = query.verify_password(check=check)

                if auth:

                    rol = rolUser(Login_model.get_role(check[3]), check[1])

                    return jsonify({'Message':f'Welcome {rol} {check[1]}'}), 200

                else:

                    return jsonify({'Message':'Your Password is Incorret, Please, Try Again'}), 400
            else:

                return jsonify({'Message':'Your User Name is Incorret'}), 400

        elif isinstance(check,BaseException):
            print("Error",check)
            return jsonify({"information": str(check)}), 500

        else:

            return jsonify({'Message':'Unregistered usert'}), 404