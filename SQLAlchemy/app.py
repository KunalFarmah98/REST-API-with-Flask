from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT
from Resources.item import Item,ItemList
import datetime

from security import authenticate,identity

from Resources.user import UserRegister
from Models.user import UserModel
from Models.item import ItemModel

from Resources.store import Store,StoreList

app = Flask(__name__)

# setting app secret key
app.secret_key = 'farmahg'

# Creating an api to add resources to
api = Api(app)

# Creating a JWT for auth
jwt = JWT(app,authenticate,identity)
# it will automatically create an auth endpoint that will return an access token

# turning off Flask_SQLAlchemy tracking extension to save computing resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# setting database uri, works with all type of sql distros
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

# setting token expiration time
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)


@app.before_first_request
def create_tables():
    db.create_all()

if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)