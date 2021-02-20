# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)

# api = Api(app)

# class Item(Resource):
#     def get(self, name):
#         return {"first_key":"first_val"}

# api.add_resource(Item, '/item/<string:name>')

# app.run(port=5000,debug=True)

# Required Imports
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, jsonify, current_identity
from auth import security

# Initializing Flask App
app = Flask(__name__)
# Enabling CORS
cors = CORS(app)
# Initializing/Defining JWT
jwt = JWT(app, security.authenticate, security.identity)
# Initializing/Defining API
api = Api(app)
# Extending Resource Features inside class - Defining a new resource
class HealthCheck(Resource):
    def get(self, arg_val):
        return {"first_key":arg_val}

# Adding resource to the API
api.add_resource(HealthCheck, '/healthcheck/<string:arg_val>')

# Python Assign __main__ to the file, from which application mainly starts
if __name__ == '__main__':
    print("Image containing the app file.")
    app.run(host ='0.0.0.0', port=5002,debug=True)