from user import User

users = [
    User(1,'kunal','jhasare')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id:u for u in users}

def authenticate(name,password):
    user = username_mapping.get(name,None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id= payload['identity']
    return userid_mapping.get(user_id)

