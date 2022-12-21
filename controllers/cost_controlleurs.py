from services.cost_service import *
from flask import Blueprint, request, jsonify
from controllers.publication_controlleur import return_log
import json 
from DTO.publication_encoder import *
app_publication_cost = Blueprint('cost_controlleur',__name__)

@app_publication_cost.route("/cost/get/<id>",methods=['GET', 'POST'])
def get_costs(id):
    try:
        return json.dumps(get_cost(id), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cost_contoller_error.txt")
        return ("Error with the cost fetching")
    
@app_publication_cost.route("/cost/get/",methods=['GET', 'POST'])
def get_all_cost():
    try:
        return json.dumps(get_all_costs(), cls=AlchemyEncoder)
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cost_contoller_error.txt")
        return ("Error with the cost fetching")

@app_publication_cost.route("/cost/add/",methods=['GET', 'POST'])
def add_costs():
    try:
        content = request.json
        add_cost(float(content["value"]),content["currancy"])
        return "cost added sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cost_contoller_error.txt")
        return ("Error with the cost insertion")

@app_publication_cost.route("/cost/delete/<id>",methods=['GET', 'POST'])
def delete_costs(id):
    try:
        content = request.json
        delete_cost(id)
        return "cost deleted sucessfuly"
    except Exception as Argument:
        session.rollback()
        return_log(Argument,"logs/cost_contoller_error.txt")
        return ("Error with the cost deletion")   