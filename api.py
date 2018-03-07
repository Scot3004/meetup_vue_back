from flask import Flask, request
from flask_restful import Resource, Api, abort
from functools import wraps
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_pymongo import PyMongo
from bson.json_util import loads, dumps

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)

@app.after_request
def after_request(response):
    """Adds a header to the request before after send the response
    Args:
        response (Response): Original response to add headers
    Returns:
        TYPE: Response
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

SUCESS_CODE = 200
BAD_REQUEST_CODE = 400
FILE_NO_EXISTS_CODE = 404
NO_VALID_PARAM_CODE = 422
JSON = {'Content-Type': 'application/json; charset=utf-8'}

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'scot', 'secorto'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)


def checkuser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_identity.username == 'scot':
            return func(*args, **kwargs)
        return abort(401)
    return wrapper

class HelloWorld(Resource):
    decorators = [checkuser, jwt_required()]
    def get(self):
        return {'hello': current_identity.username,
    'mi_list': ['el1', 'el2']
    }

class Imagenes(Resource):
    #decorators = [checkuser, jwt_required()]
    def get(self):
        return dumps(mongo.db.reviews.find({
        }))

    def post(self):
        return dumps(mongo.db.reviews.insert_one({
            'url': request.form["url"],
            'alt': request.form["alt"]
        }).inserted_id)

api.add_resource(HelloWorld, '/')
api.add_resource(Imagenes, '/imagenes')

if __name__ == '__main__':
    app.run(debug=True, port=3001)
