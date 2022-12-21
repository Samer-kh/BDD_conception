from persistance.inter_tables import *


class user(Base):
    ''' implémentation de la classe relatif à un utilisateur'''
    __tablename__="user"
    user_id= Column(Integer, primary_key=True)
    email = Column(String(50),nullable=False)
    publications  = relationship("publication", secondary=user_publication, back_populates="users")
    __mapper_arg__={
        "polymorphic_identity" : "user"
    }
    def __str__(self):
        return 'id : {} , email : {} '.format(self.user_id,self.email)
    
