class All_users():

    def __init__(self, _id, username, email, profile, password): 
        
        self.__id = _id
        self.__username = username
        self.__email = email
        self.__profile = profile
        self.__password = password 

    @classmethod
    def db_user_info(cls, row):
        return cls(
            _id=row[0],
            username=row[1],
            email=row[2],
            profile=row[3],
            password=row[4]
        )

    @classmethod
    def get_user_data(cls, user):
        return {
            'id': user.__id,
            'username': user.__username,
            'email': user.__email,
            'profileId': user.__profile,
            'password': user.__password
        }