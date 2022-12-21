from services.user_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log
import json 
from DTO.publication_encoder import *
app_publication_user = Blueprint('user_controlleur',__name__)

@app_publication_user.route("/user/get/<id>",methods=['GET', 'POST'])
def get_user(id):
    try:
        return json.dumps(get_users(id), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/user_contoller_error.txt")
        return ("Error with the user fetching")
    
@app_publication_user.route("/user/get/",methods=['GET', 'POST'])
def get_all_user():
    try:
        return json.dumps(get_all_users(), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/user_contoller_error.txt")
        return ("Error with the users fetching")

@app_publication_user.route("/user/add/",methods=['GET', 'POST'])
def add_users():
    try:
        content = request.json
        add_user(content["email"])
        return "user added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/user_contoller_error.txt")
        return ("Error with the user insertion")

@app_publication_user.route("/user/delete/<id>",methods=['GET', 'POST'])
def delete_users(id):
    try:
        content = request.json
        delete_user(id)
        return "user deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/user_contoller_error.txt")
        return ("Error with the user deletion")   