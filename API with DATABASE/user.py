import sqlite3
from flask_restful import Resource, reqparse

class User:

    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursror = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"

        # placeholder has to be a tuple in all cases
        result = cursror.execute(query,(username,))

        # getting the tuple from the result
        row = result.fetchone()
        if row:
            # if tuple has order same as init
            user = cls(*row)
            # alternate
            # user = cls(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user
    
    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursror = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"

        # placeholder has to be a tuple in all cases
        result = cursror.execute(query,(_id,))

        # getting the tuple from the result
        row = result.fetchone()
        if row:
            # if tuple has order same as init
            user = cls(*row)
            # alternate
            # user = cls(row[0],row[1],row[2])
        else:
            user = None

        connection.close()
        return user


# A resource to register a user
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    
    parser.add_argument('username',
    type = str,
    required=True,
    help = "Can't leave username blank") 

    parser.add_argument('password',
    type = str,
    required=True,
    help = "Can't leave password blank") 


    def post(self):  
        data = UserRegister.parser.parse_args()
        if(User.find_by_username(data['username'])):
            return {"message": "User {} alreay exists".format(data['username'])},401

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO Users VALUES (NULL,?,?)"
        
        cursor.execute(query,(data['username'],data['password']))
        
        connection.commit()
        connection.close()
        
        return {"message":"Created user {} successfully".format(data['username'])},201


