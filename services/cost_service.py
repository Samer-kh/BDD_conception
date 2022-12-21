''' this file contains the functions that handle all the operation related to the costs
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.cost import *

def get_cost(id):
        return session.get(cost, id)
def get_all_costs():
        return session.query(cost).all()
def add_cost(value,currancy):
        costs = cost(value=value,currancy=currancy)
        session.add(costs)
        session.commit()

def delete_cost(id):
        cost_to_delete = session.get(cost, id)
        session.delete(cost_to_delete)
        session.commit()