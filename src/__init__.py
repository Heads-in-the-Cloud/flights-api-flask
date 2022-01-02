from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

##################
# Initialization #
##################

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('DB_TYPE')}://{os.getenv('DB_USERNAME')}:" \
                                        f"{os.getenv('DB_PASSWORD')}@" \
                                        f"{os.getenv('DB_ADDRESS')}/{os.getenv('DB_NAME')}"
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

ma = Marshmallow()
ma.init_app(app)

from src.resources import api
api.init_app(app)
