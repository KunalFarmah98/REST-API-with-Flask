import sqlite3
from flask import Flask,request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required

# Every Resource is a Class extending Resource

class Item (Resource):

    # defining a parser t parse only the required request data
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required = True,
    help = "can't leave this blank vitch")

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query  = "SELECT * FROM Items WHERE name = ?"

        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if(row):
            return {"item":{'name' : row[0], 'price': row[1]}},201

    @classmethod 
    def insert(cls,item):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query  = "INSERT INTO Items VALUES(?,?)"

        cursor.execute(query,(item['name'],item['price']))
        
        connection.commit()
        connection.close()
    
    @classmethod 
    def update(cls,item):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query  = "UPDATE Items SET price = ? WHERE name = ?"

        cursor.execute(query,(item['price'],item['name']))
        
        connection.commit()
        connection.close()

    # this makes this endpoint authorization specific
    # we need to send the jwt access token in the header of the request
    @jwt_required()
    def get(self,name):

        item = self.find_by_name(name)

        if(item):
            return item
        else:
            return {'message': 'Item not found'},404


    def post(self,name):

        if(self.find_by_name(name)):
            return {'message': "Item with name {} already exists".format(name)},400

        data = Item.parser.parse_args()

        new_item = {'name':name, 'price':data['price']}
        
        try:
            self.insert(new_item)
        except:
            return {'message': 'Error inserting item'},500        

        return new_item,201

    def delete(self, name):
        item = self.find_by_name(name)
        if(item is None):
            {'message': 'item does not exist'}
        
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query  = "DELETE FROM Items WHERE name = ?"

        cursor.execute(query,(name,))
        
        connection.commit()
        connection.close()
        return {'deleted item': item},201

    def put(self, name):
        # parsing required arguments only instead of entire json
        data = Item.parser.parse_args()
        # data = request.get_json()
        item = self.find_by_name(name)
        new_item = {'name':name,'price':data['price']}
        if(item):
            self.update(new_item) 
            return {'updated':item},201
        else:
            self.insert(new_item)
            return {'created':new_item},201


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query  = "SELECT * FROM Items"

        result = cursor.execute(query)
        items=[]
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        
        connection.close()

        return {'items':items}

