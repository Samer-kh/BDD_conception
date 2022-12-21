from services.author_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log
import json 
from DTO.publication_encoder import *
app_publication_author = Blueprint('author_controlleur',__name__)

@app_publication_author.route("/author/get/<id>",methods=['GET', 'POST'])
def get_author(id):
    try:
        return json.dumps(get_authors(id), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/author_contoller_error.txt")
        return ("Error with the author fetching")
    
@app_publication_author.route("/author/get/",methods=['GET', 'POST'])
def get_all_author():
    try:
        return json.dumps(get_all_authors(), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/author_contoller_error.txt")
        return ("Error with the author fetching")

@app_publication_author.route("/author/add/",methods=['GET', 'POST'])
def add_author():
    try:
        content = request.json
        add_authors(content["name"])
        return "author added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/author_contoller_error.txt")
        return ("Error with the author insertion")

@app_publication_author.route("/author/delete/<id>",methods=['GET', 'POST'])
def delete_author(id):
    try:
        content = request.json
        delete_authors(id)
        return "author deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/author_contoller_error.txt")
        return ("Error with the author deletion")   