''' this file contains the functions that handle all the operation related to the categories
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.category import *

def get_categories(id):
        return session.get(category, id)
def get_all_cat():
        return session.query(category).all()
def add_cat(name_category):
        categ = category(name_category=name_category)
        session.add(categ)
        session.commit()

def delete_cat(id):
        cat_to_delete = session.get(category, id)
        session.delete(cat_to_delete)
        session.commit()