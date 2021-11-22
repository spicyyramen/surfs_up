#import flask dependency
from typing_extensions import runtime
from flask import Flask

# create new flask instance 
app=Flask(__name__)

# create first route and associated function
@app.route('/')
def hello_world():
    return 'Hello world'

