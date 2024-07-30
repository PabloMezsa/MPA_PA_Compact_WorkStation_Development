from flask import session

def rolUser(rol, userName):

    if rol == 'Administrador':

        session['rolSA'] = rol
        session['userName'] = userName

        return 'Administrador'
    
    else:

        session['User'] = rol
        session['userName'] = userName

        return 'User'