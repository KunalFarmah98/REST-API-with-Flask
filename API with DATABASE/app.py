from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from item import Item,ItemList
import datetime

from security import authenticate,identity

from user import UserRegister

app = Flask(__name__)

# setting app secret key
app.secret_key = 'farmahg'

# Creating an api to add resources to
api = Api(app)

# Creating a JWT for auth
jwt = JWT(app,authenticate,identity)
# it will automatically create an auth endpoint that will return an access token

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')

# setting token expiration time
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)

if __name__=='__main__':
    app.run(debug=True)