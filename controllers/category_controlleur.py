from services.category_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log
import json 
from DTO.publication_encoder import *
app_publication_cat = Blueprint('category_controlleur',__name__)

@app_publication_cat.route("/cat/get/<id>",methods=['GET', 'POST'])
def get_cat(id):
    try:
        return json.dumps(get_categories(id), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cat_contoller_error.txt")
        return ("Error with the category fetching")
    
@app_publication_cat.route("/cat/get/",methods=['GET', 'POST'])
def get_all_cat():
    try:
        return json.dumps(get_all_cat(), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cat_contoller_error.txt")
        return ("Error with the category fetching")

@app_publication_cat.route("/cat/add/",methods=['GET', 'POST'])
def add_author():
    try:
        content = request.json
        add_cat(content["name_category"])
        return "author added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cat_contoller_error.txt")
        return ("Error with the category insertion")

@app_publication_cat.route("/cat/delete/<id>",methods=['GET', 'POST'])
def delete_author(id):
    try:
        content = request.json
        delete_cat(id)
        return "author deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cat_contoller_error.txt")
        return ("Error with the category deletion")   