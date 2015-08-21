import os
from flask import Flask, request


app = Flask(__name__)

# Routes
@app.route('/')
def _index():
    from routes.index import Index
    return Index().route(request)
    
@app.route('/mms', methods=['POST'])
def _mms():
    from routes.mms import MMS
    return MMS().route(request)

# Main
if __name__ == "__main__":
    app.run(debug=True)
