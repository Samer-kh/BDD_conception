from persistance.user import *
from persistance.inter_tables import *
from persistance.Lab import *

def add_Lab_to_users_notif(id_lab,id_user):
    lab_to_add = session.get(lab, id_lab)
    user_effected = session.get(user, id_user)
    user_effected.labs_notif.append(lab_to_add)
    
    session.add(user_effected)
    session.commit()
    
def add_user_to_lab_notif(id_lab,id_user):
    lab_effected = session.get(lab, id_lab)
    user_to_add = session.get(user, id_user)
    lab_effected.users_notif.append(user_to_add)
    
    session.add(lab_effected)
    session.commit()  
    
def get_all_user_lab_notif():
    return session.query(user_lab_notif).all()  