''' this file contains the functions that handle all the operation related to the costs
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.exchange import *

def get_echange(id):
        try:
                return session.get(exchange, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_exchange():
        return session.query(exchange).all()
def add_echange(euro_to_dollars,pound_to_dollars,euro_to_pounds):
        try:
                echanges = exchange(euro_to_dollar=euro_to_dollars,pound_to_dollar=pound_to_dollars,euro_to_pound=euro_to_pounds)
                session.add(echanges)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception("cannot add the row")

def delete_echange(id):
        try:
                cost_to_delete = session.get(exchange, id)
                session.delete(cost_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception("cannot delete the row")        
def update_echange(dict,id):
        try:
                cost_to_update = session.get(exchange, id)
                cost_to_update.euro_to_dollar=dict["euro_to_dollar"]  
                cost_to_update.pound_to_dollar=dict["pound_to_dollar"]
                cost_to_update.euro_to_pound=dict["euro_to_pound"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()