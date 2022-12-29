from persistance.inter_tables import *


class cost(Base):
    ''' implémentation de la classe relatif à un cout'''
    __tablename__="cost"
    cost_id= Column(Integer, primary_key=True)
    value = Column(Float,nullable=False)
    currancy=Column(String(10),nullable=False)
    book = relationship("regular_books", uselist=False, back_populates="costs")
    periodics = relationship("periodics", uselist=False, back_populates="costs")
    __mapper_arg__={
        "polymorphic_identity" : "cost"
    }
    def __str__(self):
        return 'id : {} , value : {} , currancy : {}'.format(self.cost_id,self.value,self.currancy)
    @staticmethod
    def  getAttributes():
        return {"cost_id":"int","value":"float","currancy":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"currancy":["Dollar", "Euro","Pound"]}   
          
