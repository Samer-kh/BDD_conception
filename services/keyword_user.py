from persistance.user import *
from persistance.inter_tables import *
from persistance.keyword import *

def add_key_to_users_(id_key,id_user):
    key_to_add = session.get(keyword, id_key)
    user_effected = session.get(user, id_user)
    user_effected.keywords_u.append(key_to_add)
    
    session.add(user_effected)
    session.commit()
    
def add_user_to_key(id_key,id_user):
    key_effected = session.get(keyword, id_key)
    user_to_add = session.get(user, id_user)
    key_effected.users_d.append(user_to_add)
    
    session.add(key_effected)
    session.commit()   
    
def get_all_key_user():
    return session.query(keyword_user).all()  