from persistance.publication import *
from persistance.inter_tables import *
from persistance.keyword import *

def add_key_to_pub(id_key,id_pub):
    key_to_add = session.get(keyword, id_key)
    pub_effected = session.get(publication, id_pub)
    pub_effected.keywords_p.append(key_to_add)
    
    session.add(pub_effected)
    session.commit()
    
def add_pub_to_key(id_key,id_pub):
    key_effected = session.get(keyword, id_key)
    pub_to_add = session.get(publication, id_pub)
    key_effected.pubs.append(pub_to_add)
    
    session.add(key_effected)
    session.commit()   