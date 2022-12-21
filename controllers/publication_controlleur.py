''' In this file, we provide all the endpoints related to the publications to be consumed by the front_end 
'''
from services.publication_service import *
from flask import Blueprint, request, jsonify
import json
from DTO.publication_encoder import *
app_publication = Blueprint('publication_controlleur',__name__)


''' register the error into a certain file as a log'''

def return_log(argument,file_name):
        f = open(file_name, "a")
        # writing in the file
        f.write("\n "+str(argument))
        # closing the file
        f.close()

''' endpoints for fetching differents document from the dataBase'''

@app_publication.route("/publication/book/get/<id>",methods=['GET', 'POST'])
def get_regualr_book():
    try:
        book=get_regular_books(id)
        return json.dumps(book, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the book fetching")
    
@app_publication.route("/publication/periodic/get/<id>",methods=['GET', 'POST'])
def get_periodic():
    try:
        periodic=get_periodics(id)
        return  json.dumps(periodic, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the periodic fetching")
    
@app_publication.route("/publication/internal/get/<id>",methods=['GET', 'POST'])
def get_internal_report():
    try:
        content = request.json
        scientific_report=get_internal_reports(id)
        return json.dumps(scientific_report, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the internal_report fetching")

@app_publication.route("/publication/ecl/get/<id>",methods=['GET', 'POST'])
def get_ecl_thesis():
    try:
        ecl_thesis=get_ECL_thesis(id)
        return json.dumps(ecl_thesis, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the ecl thesis fetching")
 
@app_publication.route("/publication/scientific/get/<id>",methods=['GET', 'POST'])
def get_scientific_report():
    try:
        sci_rep=get_scientific_reports(id)
        return json.dumps(sci_rep, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the scientific report fetching")

''' endpoints for fetching differents document from the dataBase ( all documents)'''

@app_publication.route("/publication/book/get",methods=['GET', 'POST'])
def get_all_regualr_book():
    try:
        book=get_regular_books_all()
        return json.dumps(book, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the book fetching")
    
@app_publication.route("/publication/periodic/get",methods=['GET', 'POST'])
def get_all_periodic():
    try:
        periodic=get_periodics_all()
        return json.dumps(periodic, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the periodic fetching")
    
@app_publication.route("/publication/internal/get",methods=['GET', 'POST'])
def get_all_internal_report():
    try:
        scientific_report=get_internal_reports_all()
        return json.dumps(scientific_report, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the internal_report fetching")

@app_publication.route("/publication/ecl/get",methods=['GET', 'POST'])
def get_all_ecl_thesis():
    try:
        ecl_thesis=get_ECL_thesis_all()
        return json.dumps(ecl_thesis, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the ecl thesis fetching")
 
@app_publication.route("/publication/scientific/get",methods=['GET', 'POST'])
def get_all_scientific_report():
    try:
        sci_rep=get_scientific_reports_all()
        return json.dumps(sci_rep, cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the scientific report fetching")
      

''' endpoints for adding different documents into the database'''

@app_publication.route("/publication/book/add/",methods=['GET', 'POST'])
def add_regualr_book():
    try:
        content = request.json
        add_regular_books(content["state"],content["title"],content["publisher"],content["edition"]
                          ,content["year_publication"],content["book_shop"],content["cost_id"])
        return "book added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the book insertion")
    
@app_publication.route("/publication/periodic/add/",methods=['GET', 'POST'])
def add_periodic():
    try:
        content = request.json
        add_periodics(content["state"],content["volume"],content["publisher"],content["edition"]
                          ,content["year_publication"],content["book_shop"],content["cost_id"])
        return "periodic added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the periodic insertion")
    
@app_publication.route("/publication/internal/add/",methods=['GET', 'POST'])
def add_internal_report():
    try:
        content = request.json
        add_internal_reports(content["state"],content["title"],content["year_publication"])
        return "internal report added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the internal_report insertion")

@app_publication.route("/publication/ecl/add/",methods=['GET', 'POST'])
def add_ecl_thesis():
    try:
        content = request.json
        add_ECL_thesis(content["state"],content["title"],content["author_id"],content["year_publication"])
        return "ecl thesis added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the ecl thesis insertion")
 
@app_publication.route("/publication/scientific/add/",methods=['GET', 'POST'])
def add_scientific_report():
    try:
        content = request.json
        add_scientific_reports(content["state"],content["title"],content["year_publication"])
        return "scientific report added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the scientific report insertion")
    
''' endpoints for the deletion of differents documents out of the database'''  
      
@app_publication.route("/publication/book/delete/<id>",methods=['GET', 'POST'])
def delete_regualr_book(id):
    try:
        delete_regular_books(id)
        return "book deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the book deletion")
    
@app_publication.route("/publication/periodic/delete/<id>",methods=['GET', 'POST'])
def delete_periodic(id):
    try:
        delete_periodics(id)
        return "peridic deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the periodic deletion")
    
@app_publication.route("/publication/internal/delete/<id>",methods=['GET', 'POST'])
def delete_internal_reprots(id):
    try:
        delete_internal_reports(id)
        return "internal report deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the internal report deletion")

@app_publication.route("/publication/ecl/delete/<id>",methods=['GET', 'POST'])
def delete_ecl_thesis(id):
    try:
        delete_ecl_thesiss(id)
        return "ecl thesis deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the ecl thesis deletion")

@app_publication.route("/publication/scientific/delete/<id>",methods=['GET', 'POST'])
def delete_scientific_report(id):
    try:
        delete_scientific_reports(id)
        return "scientific report deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the scientific report deletion")
            
@app_publication.route("/publication/book/update/<id>",methods=['GET', 'POST'])
def update_regular_books(id):
    try:
        content = request.json
        update_regular_book(content,id)
        return "regular book updated sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the update of the regular book")
    
@app_publication.route("/publication/periodic/update/<id>",methods=['GET', 'POST'])
def update_periodic(id):
    try:
        content = request.json
        update_periodic(content,id)
        return "periodic updated sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the update of the periodic")
    
@app_publication.route("/publication/internal/update/<id>",methods=['GET', 'POST'])
def update_internal_reports(id):
    try:
        content = request.json
        update_internal_reports(content,id)
        return "internal report updated sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/contoller_error.txt")
        return ("Error with the update of the internal report")