from flask import render_template, request
from database.db import *

def func_home_page():
    return render_template("home.html")
    
def func_register_page():
    return render_template("register.html")
    
def func_consult_page():
    return render_template("consult.html")

def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    
    save_user = add_user(id, name, lastname, birthday)
    
    return render_template("register.html")

def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    user_data = consult_user(id)
    response = ""
    if user_data != False and len(user_data) != 0:
        response = {
            'status': 'OK',
            'name': user_data[0][1]
        }
    else:
        response = {
            'status': 'error'
        }
    return response