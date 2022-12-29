''' this file contains the functions that handle all the operation related to the users
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.keyword import *

def get_keyword(id):
        try:
                return session.get(keyword, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_keywords():
        try:
                return session.query(keyword).all()
        except Exception:
                session.rollback()
                raise Exception()
def add_keyword(value):
        try:
                users = keyword(value=value)
                session.add(users)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_keyword(id):
        try:
                key_to_delete = session.get(keyword, id)
                session.delete(key_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def update_keyword(dict,id):
        try:
                users = session.get(keyword, id)
                users.value=dict["value"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()