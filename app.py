from flask import Flask
from flask_restful import Api
from resource.Items import Items, ItemsAll
import datetime
import os
import sqlite3
from db import db
import sys
from flask_cors import CORS


print(sys.path)
app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1800)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URLL","sqlite:///data.db") #"sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


api.add_resource(Items, "/")
api.add_resource(ItemsAll, "/all")

# @app.before_first_request #delet this block before posting to heroku
# def create_tables():
#     print("tables created")
#     db.create_all()

if __name__ == '__main__':
    # db.init_app(app)  #delete this before posting to heroku
    app.run(port="5000", debug=True)
