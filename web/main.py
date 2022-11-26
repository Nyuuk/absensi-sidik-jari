from flask import Flask

app = Flask(__name__)
from api.api import app as api_blueprint
app.register_blueprint(api_blueprint)
from front_end.htm import app as fe_blueprint
app.register_blueprint(fe_blueprint)
