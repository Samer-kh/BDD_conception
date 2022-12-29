''' this file contains the functions that handle all the operation related to the categories
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.category import *

def get_categories(id):
        try:
                return session.get(category, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_cat():
        return session.query(category).all()
def add_cat(name_category):
        try:
                categ = category(name_category=name_category)
                session.add(categ)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_cat(id):
        try:
                cat_to_delete = session.get(category, id)
                session.delete(cat_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def update_cat(dict,id):
        try:
                cat_to_update=session.get(category,id)
                cat_to_update.name_category=dict["name_category"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()