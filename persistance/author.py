from persistance.inter_tables import *


class author(Base):
    ''' implémentation de la classe relatif à un author'''
    __tablename__="author"
    author_id= Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    publications = relationship("Scientific_Reports", secondary=scientific_author, back_populates="authors")
    publications_books = relationship("regular_books", secondary=regular_books_author, back_populates="authors_book")
    __mapper_arg__={
        "polymorphic_identity" : "author"
    }
    def __str__(self):
        return 'id : {} , state : {} '.format(self.author_id,self.name)
    
