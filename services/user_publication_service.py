from persistance.user import *
from persistance.inter_tables import *
from persistance.publication import *

def add_publication_to_users(id_pub,id_user):
    publication_to_add = session.get(publication, id_pub)
    user_effected = session.get(user, id_user)
    user_effected.publications.append(publication_to_add)
    
    session.add(user_effected)
    session.commit()
    
def add_user_to_publication(id_pub,id_user):
    pub_effected = session.get(publication, id_pub)
    user_to_add = session.get(user, id_user)
    pub_effected.users.append(user_to_add)
    
    session.add(pub_effected)
    session.commit() 
    
def get_all_user_pub():
    return session.query(user_publication).all()    