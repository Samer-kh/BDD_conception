''' 
    In this file, we provide all the endpoints related to the relation between authors and regular books
    to be consumed by the front_end 
'''
from services.author_book_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log

app_publication_book_auth = Blueprint('book_author_controlleur',__name__)
@app_publication_book_auth.route("/book_auth/add/",methods=['GET', 'POST'])
def add_book_to_author():
    try:
        content = request.json
        add_books_to_authors(content["id_book"],content["id_author"])
        add_author_to_books(content["id_book"],content["id_author"])
        return "relation added sucessfuly"
    except Exception as Argument:
        session.rollback()
        # creating/opening a file
        return_log(Argument,"logs/book_auth_contoller_error.txt")
        return ("Error with the relation insertion")
    
