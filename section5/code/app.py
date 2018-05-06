from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
import sys

app = Flask(__name__)
app.secret_key = 'nate'
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth      We send it a username and password which gets passed to authenticate if it matches we return "user"

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


# Only run this line if the __name__ of the file is run from terminal NOT if it is imported
if __name__ == '__main__':
    app.run(port = 5000, debug=True)

#sys.path.append('/Users/Nate/Desktop/API-Course/section5/code')
#sys.path
