import os
from flask import Flask, request

from routes.index import Index
from routes.mms import MMS


app = Flask(__name__)

@app.route('/')
def _index():
    return Index().route(request)
    
@app.route('/mms')
def _mms():
    return MMS().route(request)

if __name__ == "__main__":
    app.run(debug=True)
