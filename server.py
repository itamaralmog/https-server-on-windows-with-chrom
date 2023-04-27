# https://help.bizagi.com/bpm-suite/en/index.html?subjectaltname_support.htm#ca

from flask import Flask

# create a server instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!!!"

# run the server
app.run(host="0.0.0.0", port=5684, debug=True, ssl_context=('cert.pem', 'key.pem'))