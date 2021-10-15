from flask import request,Flask
from gevent import pywsgi

app = Flask(__name__, static_folder="templates")

server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
# server.serve_forever()
server.stop()
server.close()