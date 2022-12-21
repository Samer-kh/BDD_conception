''' this file contains the functions that handle all the operation related to the users
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.user import *

def get_users(id):
        return session.get(user, id)
def get_all_users():
        return session.query(user).all()
def add_user(email):
        users = user(email=email)
        session.add(users)
        session.commit()

def delete_user(id):
        user_to_delete = session.get(user, id)
        session.delete(user_to_delete)
        session.commit()