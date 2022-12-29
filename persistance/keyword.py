from persistance.inter_tables import *


class keyword(Base):
    ''' implémentation de la classe relatif à un keyword'''
    __tablename__="keyword"
    key_id= Column(Integer, primary_key=True)
    value = Column(String(50),nullable=False)
    users_d  = relationship("user", secondary=keyword_user, back_populates="keywords_u")
    pubs  = relationship("publication", secondary=keyword_publication, back_populates="keywords_p")
    __mapper_arg__={
        "polymorphic_identity" : "keyword"
    }
    def __str__(self):
        return 'id : {} , value : {} '.format(self.key_id,self.value)
    @staticmethod
    def  getAttributes():
        return {"key_id":"int","value":"str"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {}     
