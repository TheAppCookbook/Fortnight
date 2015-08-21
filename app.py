### Ignore this
if __name__ == "__main__":
    import sys
    sys.dont_write_bytecode = True
### Prevents file clutter

import os
from flask import Flask, request

from routes.index import Index
from routes.mms import MMS


app = Flask(__name__)

# Routes
@app.route('/', methods=Index.methods)
def _index():
    return Index().route(request)
    
@app.route('/mms', methods=MMS.methods)
def _mms():
    return MMS().route(request)

if __name__ == "__main__":
    app.run(debug=True)
