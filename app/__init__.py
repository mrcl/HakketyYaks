from flask import Flask
from flask_wtf.csrf import CSRFProtect
# from flask_pymongo import PyMongo

# Flask Initialisation
app = Flask(__name__)
app.config.from_object('config')

# Load config.py file
csrf = CSRFProtect(app)

# Plugins Initialisation
# mongo = PyMongo(app)

from app import views
