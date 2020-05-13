from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# DS to store data. Looks like
""" stores = [
                {
                "name":name,
                "items":[
                        {
                            "name":itemname,
                            "price":itemprice
                        }
                        ]  
                }
            ] 
"""

stores=[]

""" Server's POV """
# POST is used to receive data
# GET is used to send data

# home url running on the html render
@app.route('/')
def home():
    return "Hello"



# POST/ store data: {name:} 
@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name':request_data['name'],
                'items':[]
                }
    stores.append(new_store)
    return jsonify(new_store) 



# GET /store/<string:name>
@app.route('/store/<string:name>')
def  get_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'Erorr': "Store not found"})




# GET /store
@app.route('/store')
def  get_stores():
    # JSON is a dict and out ds is a list, so we add that list
    # to a new dictionary and convert it to json
    return jsonify({'stores':stores})



# POST /store/<string:name>/item {name:,prince:}
@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item = {'name':request_data['name'],
                        'price':request_data['price']
                    }
        store['items'].append(new_item)
        return jsonify(new_item)
    return jsonify({'Erorr': "Store not found"})
    


# GET /store/<string:name>/ item {name:,price:}
@app.route('/store/<string:name>/item')
def  get_items_in_store(name):
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return jsonify({'Erorr': "Store not found"})

