''' this file contains the functions that handle all the operation related to the authors 
    Operations supported : 
        add , modify , delete

'''

from persistance.inter_tables import *
from persistance.author import *

def get_authors(id):
        return session.get(author, id)
def get_all_authors():
        return session.query(author).all()
def add_authors(names):
        authors = author(name=names)
        session.add(authors)
        session.commit()
def update_author(dict,id):
        auther_to_update = session.get(author, id)
        for i in list(dict.keys()):
                auther_to_update.i = dict[i]
        session.commit()
def delete_authors(id):
        author_to_delete = session.get(author, id)
        session.delete(author_to_delete)
        session.commit()