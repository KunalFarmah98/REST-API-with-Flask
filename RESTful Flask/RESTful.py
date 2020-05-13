from flask import Flask,jsonify,request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app = Flask(__name__)

# setting app secret key
app.secret_key = 'farmahg'

# Creating an api to add resources to
api = Api(app)

# Creating a JWT for auth
jwt = JWT(app,authenticate,identity)
# it will automatically create an auth endpoint that will return an access token


# DS to store items

items=[]

# Every Resource is a Class extending Resource

class Item (Resource):

    # defining a parser t parse only the required request data
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required = True,
    help = "can't leave this blank vitch")
    
    # this makes this endpoint authorization specific
    # we need to send the jwt access token in the header of the request
    @jwt_required()
    def get(self,name):

    """ for item in items:
            if(item['name']==name):
                return item """

        # using in-built filter function to find the item using lambda function
        # next gets the next item found, None makes it return None as default if no next item is there
        item = next(filter(lambda x: x['name']==name,items),None)
        return {'item':item}, 201 if item else 404

        # # return a response code for better understanding
        # return {"item":None},404

    def post(self,name):
        
        """ DO NOT LOAD DATA BEFORE CHECKING FOR ERRORS AS IT MAY EVEN NOT BE REQUIRED"""
    
        if(next(filter(lambda x:x['name']==name,items),None)):
            return {'message': "Item with name {} already exists".format(name)},400

        data = request.get_json(silent=True)
        new_item = {'name':name, 'price':data['price']}
        items.append(new_item)
        # return a response code for better understanding
        return new_item,201

    def delete(self, name):
        item = next(filter(lambda x: x['name']==name,items),None)
        if(item):
            items.remove(item)
        return {'deleted item': item}

    def put(self, name):
        # parsing required arguments only instead of entire json
        data = Item.parser.parse_args()
        # data = request.get_json()
        item = next(filter(lambda x: x['name']==name,items),None)
        if(item):
            #item['price'] = data['price']
            item.update(data)
            return {'updated':item},201
        else:
            new_item = {'name':name,'price':data['price']}
            items.append(new_item)
            return {'created':new_item},201

api.add_resource(Item,'/item/<string:name>')


class ItemList(Resource):
    def get(self):
        return {'Items':items}

api.add_resource(ItemList,'/items')

app.run(debug=True)