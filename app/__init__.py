from flask import Flask
# from flask.ext.pymongo import PyMongo
from mongoengine import connect

app = Flask(__name__)
app.config.from_object('config')
# mongo = PyMongo(app)
connect('project1')

from app import views
