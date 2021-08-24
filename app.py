# import flask dependency
from flask import Flask

# create new Flask app instance
app = Flask(__name__)

# create route
@app.route('/')
def hello_world():
    return 'Hello world'