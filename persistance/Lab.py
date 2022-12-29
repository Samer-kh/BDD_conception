from persistance.inter_tables import *


class lab(Base):
    ''' implémentation de la classe relatif à un laboratoire'''
    __tablename__="lab"
    lab_id= Column(Integer, primary_key=True)
    lab_name = Column(String(50),nullable=False)
    pubs = relationship("publication", back_populates="labs")
    users_auth  = relationship("user", secondary=user_lab_auth, back_populates="labs_auth")
    users_notif  = relationship("user", secondary=user_lab_notif, back_populates="labs_notif")
    books_copy = relationship("publication", secondary=pub_lab_hascopy, back_populates="labs_with_copy")
    __mapper_arg__={
        "polymorphic_identity" : "lab"
    }
    def __str__(self):
        return 'id : {} , name : {} '.format(self.lab_id,self.lab_name)
    @staticmethod
    def  getAttributes():
        return {"lab_id":"int","lab_name":"str"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {}     
