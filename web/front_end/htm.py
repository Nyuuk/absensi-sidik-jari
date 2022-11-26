from flask import Blueprint, render_template
import api.modul as mdl
from api.api import engine

app = Blueprint("web", __name__)

@app.route("/")
def wellcome():
    return render_template('index.html')

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")
    
@app.route("/add_sidikjari", methods=["GET", "POST"])
def list_sidikjari_add():
    return render_template("list_add_sidikjari.html", fingers = mdl.list_all_data_add_sidikjari(engine, "f_sidikjari"))