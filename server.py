from flask import Flask, render_template, request
from database.db import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/register_page")
def register_page():
    return render_template("register.html")
    
@app.route("/consult_page")
def consult_page():
    return render_template("consult.html")

@app.route("/register_user", methods=["post"])
def register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    
    print("id: " + id, "name: " + name, "lastname: " + lastname, "birthday: " + birthday)
    return "OK"
        
if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host, port)