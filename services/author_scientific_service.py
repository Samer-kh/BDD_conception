from persistance.author import *
from persistance.inter_tables import *
from persistance.publication import *

def add_scientific_to_authors(id_scientific,id_author):
    scientific_to_add = session.get(Scientific_Reports, id_scientific)
    author_effected = session.get(author, id_author)
    author_effected.publications.append(scientific_to_add)
    
    session.add(author_effected)
    session.commit()
    
def add_author_to_scientifics(id_scientific,id_author):
    scientific_effected = session.get(Scientific_Reports, id_scientific)
    author_to_add = session.get(author, id_author)
    scientific_effected.authors.append(author_to_add)
    
    session.add(scientific_effected)
    session.commit() 

def get_all_auth_sci():
    return session.query(scientific_author).all()  