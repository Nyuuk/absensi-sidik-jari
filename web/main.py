from flask import Flask

app = Flask(__name__)
from api.api import app as api_blueprint
app.register_blueprint(api_blueprint)