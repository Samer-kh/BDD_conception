from persistance.inter_tables import *


class exchange(Base):
    ''' implémentation de la classe relatif à un exchange'''
    __tablename__="exchange"
    exchange_id= Column(Integer, primary_key=True)
    euro_to_dollar = Column(Float,nullable=False)
    pound_to_dollar=Column(Float,nullable=False)
    euro_to_pound=Column(Float,nullable=False)
    cost = relationship("cost", uselist=False, back_populates="echanges")
    __mapper_arg__={
        "polymorphic_identity" : "exchange"
    }
    @staticmethod
    def  getAttributes():
        return {"exchange_id":"int","euro_to_dollar":"float","pound_to_dollar":"float","euro_to_pound":"float"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {}   
          
