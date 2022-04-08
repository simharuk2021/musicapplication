from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# environment variable was exported using below run in terminal:
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI") 

db = SQLAlchemy(app)

from application import routes