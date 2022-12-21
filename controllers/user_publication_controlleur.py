''' 
    In this file, we provide all the endpoints related to the relation between users and publications 
    to be consumed by the front_end 
'''
from services.user_publication_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log

app_publication_user_publication = Blueprint('user_publication_controlleur',__name__)
@app_publication_user_publication.route("/user_pub/add/",methods=['GET', 'POST'])
def add_user_to_pub():
    try:
        content = request.json
        add_publication_to_users(content["id_pub"],content["id_user"])
        add_user_to_publication(content["id_pub"],content["id_user"])
        return "relation added sucessfuly"
    except Exception as Argument:
        session.rollback()
        # creating/opening a file
        return_log(Argument,"logs/user_publication_contoller_error.txt")
        return ("Error with the relation insertion")
    
