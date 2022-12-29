from persistance.inter_tables import *


class category(Base):
    ''' implémentation de la classe relatif à une categorie'''
    __tablename__="categories"
    Category_id= Column(Integer, primary_key=True)
    name_category = Column(String(50),nullable=False)
    books = relationship("regular_books", secondary=regular_books_category, back_populates="book_categories")

    __mapper_arg__={
        "polymorphic_identity" : "category"
    }
    def __str__(self):
        return 'id : {} , name : {} '.format(self.Category_id,self.name_category)
    @staticmethod
    def  getAttributes():
        return {"Category_id":"int","name_category":"str"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {}   

