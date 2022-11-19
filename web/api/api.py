from flask import Blueprint, jsonify, request
from sqlalchemy import create_engine

app = Blueprint("api", __name__)

# database
IP_DATABASE = "10.42.0.1"
PORT_DATABASE = 5432
USER_DATABASE = "uss_ppnh"
PASSWORD_DATABASE = "ppnh2007"
DATABASE_NAME = "ppnh"
SANTRI_PUTRA_TABLE = "santri_putra"
engine = create_engine("postgresql://{}:{}@{}/{}".format(USER_DATABASE, PASSWORD_DATABASE, IP_DATABASE, DATABASE_NAME))

@app.route("/api")
def hello():
    return "Hello World", 200

@app.route("/api/sidikjari")
def sidik_jari():
    headers = request.headers
    