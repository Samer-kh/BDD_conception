''' this file contains the functions that handle all the operation related to the users
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.user import *

def get_users(id):
        try:
                return session.get(user, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_users():
        try:
                return session.query(user).all()
        except Exception:
                session.rollback()
                raise Exception()
def add_user(email):
        try:
                users = user(email=email)
                session.add(users)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_user(id):
        try:
                user_to_delete = session.get(user, id)
                session.delete(user_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def update_user(dict,id):
        try:
                users = session.get(user, id)
                users.email=dict["email"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()