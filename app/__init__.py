from flask import Flask, jsonify
from flask_pymongo import PyMongo
from utils.JSONEncoder import JSONEncoder

api = Flask(__name__)
api.config['MONGO_URI'] = 'mongodb://<username>:<password>@<domain>:27017/mnemosyne'        # @TODO: extract to environment variable
api.config['DEBUG'] = True                                                                  # @TODO: extract to environment variable
api.config['SECRET_KEY'] = '<CHANGETHIS>'                                                   # @TODO: extract to environment variable
mongo = PyMongo(api)
api.json_encoder = JSONEncoder

from app.views import honeypotRoutes
from app.mitre import mitreRoutes
api.register_blueprint(honeypotRoutes)
api.register_blueprint(mitreRoutes)

@api.route('/')
def home():
    return jsonify({'success': 'true', 'response': 'api reached'}), 200
