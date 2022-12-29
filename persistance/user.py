from persistance.inter_tables import *


class user(Base):
    ''' implémentation de la classe relatif à un utilisateur'''
    __tablename__="user"
    user_id= Column(Integer, primary_key=True)
    email = Column(String(50),nullable=False)
    publications  = relationship("publication", secondary=user_publication, back_populates="users")
    labs_auth  = relationship("lab", secondary=user_lab_auth, back_populates="users_auth")
    labs_notif  = relationship("lab", secondary=user_lab_notif, back_populates="users_notif")
    keywords_u  = relationship("keyword", secondary=keyword_user, back_populates="users_d")
    __mapper_arg__={
        "polymorphic_identity" : "user"
    }
    def __str__(self):
        return 'id : {} , email : {} '.format(self.user_id,self.email)
    @staticmethod
    def  getAttributes():
        return {"user_id":"int","email":"str"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {}     
