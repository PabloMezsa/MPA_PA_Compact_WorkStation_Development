class All_users():

    def __init__(self, _id, userName, name, lastName, number, email, identification, profile, password): 
        
        self.__id = _id
        self.__userName = userName
        self.__name = name
        self.__lastName = lastName
        self.__number = number
        self.__email = email
        self.__identification = identification
        self.__profile = profile
        self.__password = password 

    @classmethod
    def db_user_info(cls, row):
        return cls(
            _id=row[0],
            userName=row[1],
            name=row[2],
            lastName=row[3],
            number=row[4],
            email=row[5],
            identification=row[6],
            profile=row[7],
            password=row[8]
        )

    @classmethod
    def get_user_data(cls, user):
        return {
            'id': user.__id,
            'userName': user.__userName,
            'name': user.__name,
            'lastName': user.__lastName,
            'number': user.__number,
            'email': user.__email,
            'identification': user.__identification,
            'profileId': user.__profile,
            'userPassword': user.__password
        }