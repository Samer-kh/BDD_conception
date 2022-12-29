''' this file contains the functions that handle all the operation related to the labs
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.Lab import *

def get_lab(id):
        try:
                return session.get(lab, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_labs():
        try:
                return session.query(lab).all()
        except Exception:
                session.rollback()
                raise Exception()
def add_lab(lab_name):
        try:
                labs = lab(lab_name=lab_name)
                session.add(labs)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_lab(id):
        try:
                lab_to_delete = session.get(lab, id)
                session.delete(lab_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def update_lab(dict,id):
        try:
                labs = session.get(lab, id)
                labs.lab_name=dict["lab_name"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()