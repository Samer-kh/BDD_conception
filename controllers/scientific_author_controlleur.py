''' 
    In this file, we provide all the endpoints related to the relation between authors and scientific reports
    to be consumed by the front_end 
'''
from services.author_scientific_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log

app_publication_sci_auth = Blueprint('scientific_author_controlleur',__name__)
@app_publication_sci_auth.route("/sci_auth/add/",methods=['GET', 'POST'])
def add_scientific_to_author():
    try:
        content = request.json
        add_scientific_to_authors(content["id_scientific"],content["id_author"])
        add_author_to_scientifics(content["id_scientific"],content["id_author"])
        return "relation added sucessfuly"
    except Exception as Argument:
        session.rollback()
        # creating/opening a file
        return_log(Argument,"logs/sci_auth_contoller_error.txt")
        return ("Error with the relation insertion")
    
