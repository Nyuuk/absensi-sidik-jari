from flask import Blueprint, jsonify, request, redirect
from sqlalchemy import create_engine
from os import path
import sys
import json
import api.modul as mdl
# import front_end.htm as htm

app = Blueprint("api", __name__)

# database
IP_DATABASE = "10.42.0.1"
PORT_DATABASE = 5432
USER_DATABASE = "uss_ppnh"
PASSWORD_DATABASE = "ppnh2007"
DATABASE_NAME = "ppnh"
SANTRI_PUTRA_TABLE = "santri_putra"
engine = create_engine("postgresql://{}:{}@{}/{}".format(USER_DATABASE, PASSWORD_DATABASE, IP_DATABASE, DATABASE_NAME))

JSON_Sett = "setting.json"

# Setting json
if not path.exists(JSON_Sett):
    sys.exit("File setting.json not found")

with open(JSON_Sett, 'r') as js:
    set_data = json.load(js)
#############

@app.route("/api")
def hello():
    return "Hello World", 200

@app.route("/api/sidikjari", methods=['POST', 'GET', 'DELETE'])
def sidik_jari():
    headers = request.headers
    if request.method == "DELETE":
        te = mdl.del_data_in_tb(engine, "f_sidikjari", {"by": "id", "value": request.arg.get("id")})
        # if te:
        return redirect("/add_sidikjari")
        # else:
            
    if request.method == "POST":
        # Menambahkan sidik jari
        if set_data['type'] == "add_sidikjari":
            #pass
            frmt = ['finger', 'time_push']
            val = [request.form.get('finger'), mdl.now_time()]
            mdl.insert_to_table(engine, set_data['tb_name'], frmt,val)
            return 'Ok', 200
        # Absen Ta'lim Subuh
        if set_data['type'] == "ATSubuh":
            pass
        # Absen Ta'lim Ashar
        if set_data['type'] == "ATAshar":
            pass
        # Absen Sholat Jama'ah Subuh
        if set_data['type'] == "ASJSubuh":
            pass
        # Absen Sholat Jama'ah Dhohor
        if set_data['type'] == "ASJDhohor":
            pass
        # Absen Sholat Jama'ah Ashar
        if set_data['type'] == "ASJAshar":
            pass
        # Absen Sholat Jama'ah Maghrib
        if set_data['type'] == "ASJMaghrib":
            pass
        # Absen Sholat Jama'ah Isha
        if set_data['type'] == "ASJIsha":
            pass
        else:
            return "Not Found", 302
