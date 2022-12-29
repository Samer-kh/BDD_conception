''' this file contains the functions that handle all the operation related to the costs
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.cost import *

def get_cost(id):
        try:
                return session.get(cost, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_costs():
        return session.query(cost).all()
def add_cost(value,currancy):
        try:
                costs = cost(value=value,currancy=currancy)
                session.add(costs)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception("cannot add the row")

def delete_cost(id):
        try:
                cost_to_delete = session.get(cost, id)
                session.delete(cost_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception("cannot delete the row")        
def update_cost(dict,id):
        try:
                cost_to_update = session.get(cost, id)
                cost_to_update.value=dict["value"]  
                cost_to_update.currancy=dict["currancy"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()