import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dbmappper

# Get the underlying Flask app instance
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

dbmappper.DbEngine()
# Create the SqlAlchemy db instance
db = SQLAlchemy(app)