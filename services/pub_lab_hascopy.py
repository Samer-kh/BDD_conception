from persistance.publication import *
from persistance.inter_tables import *
from persistance.Lab import *

def add_pub_to_lab(id_pub,id_lab):
    pub_to_add = session.get(publication, id_pub)
    lab_effected = session.get(user, id_lab)
    lab_effected.books_copy.append(pub_to_add)
    
    session.add(lab_effected)
    session.commit()
    
def add_lab_to_pub(id_pub,id_lab):
    pub_effected = session.get(publication, id_pub)
    lab_to_add = session.get(lab, id_lab)
    pub_effected.labs_with_copy.append(lab_to_add)
    
    session.add(pub_effected)
    session.commit()   