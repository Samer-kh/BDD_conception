''' this file contains the functions that handle all the operation related to the authors 
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.author import *

def get_authors(id):
        try:
                return session.get(author, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_all_authors():
        return session.query(author).all()
def add_authors(names):
        try:
                authors = author(name=names)
                session.add(authors)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
def update_author(dict,id):
        try:
                auther_to_update = session.get(author, id)
                auther_to_update.name=dict["name"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
def delete_authors(id):
        try:
                author_to_delete = session.get(author, id)
                session.delete(author_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()