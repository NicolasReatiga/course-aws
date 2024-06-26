from flask import render_template, request
from database.db import *
from controller.adminS3 import *

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
    photo = request.files["photo"]
    
    save_user = add_user(id, name, lastname, birthday)
    
    if save_user:
        s3_resource = connection_s3()
        origin_path = save_file(photo)
        confirm_upload = upload_file(s3_resource, origin_path)
        if confirm_upload:
            return "<script>alert(" + "User added correctly" + ")</script>"
        else:
            return "<script>alert(" + "User added without photo" + ")</script>"
    else:
        return "<h1>Error: the user was not created</h1>"

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