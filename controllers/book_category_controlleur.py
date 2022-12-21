''' 
    In this file, we provide all the endpoints related to the relation between categories and regular books
    to be consumed by the front_end 
'''
from services.book_category_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log

app_publication_book_cat = Blueprint('book_category_controlleur',__name__)
@app_publication_book_cat.route("/book_cat/add/",methods=['GET', 'POST'])
def add_book_to_cat():
    try:
        content = request.json
        add_book_to_category(content["id_book"],content["id_category"])
        add_category_to_book(content["id_book"],content["id_category"])
        return "relation added sucessfuly"
    except Exception as Argument:
        session.rollback()
        # creating/opening a file
        return_log(Argument,"logs/book_auth_contoller_error.txt")
        return ("Error with the relation insertion")
    
