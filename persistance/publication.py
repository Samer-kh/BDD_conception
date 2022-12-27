from persistance.inter_tables import *
from persistance.author import *
from persistance.category import *
from persistance.cost import *
from persistance.user import *
class publication(Base):
    ''' implémentation de la classe mére relatif à la table publication'''
    __tablename__="publication"
    publication_id = Column(Integer, primary_key=True)
    year_publication = Column(Date,nullable=False)
    state = Column(String(50), nullable=False)
    users  = relationship("user", secondary=user_publication, back_populates="publications")
    __mapper_arg__={
        "polymorphic_on" : type,
        "polymorphic_identity" : "publication"
    }
    def __str__(self):
        return 'id : {} , state : {} '.format(self.publication_id,self.state)
    '''get the attributes needed for the views'''
    @staticmethod
    def  getAttributes():
        return {"publication_id":"int","year_publication":"date","state":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]}
       
class regular_books(publication):
    ''' implémentation d'une classe relatif à la table regular books '''
    __tablename__="regularbooks"

    ISBN = Column(Integer,ForeignKey("publication.publication_id"),primary_key=True)
    title = Column(String(50),nullable=False)
    publisher = Column(String(50),nullable=False)
    edition = Column(String(50),nullable=False)
    book_shop=Column(String(50),nullable=False)
    cost_id = Column(Integer,ForeignKey("cost.cost_id"),nullable=False)
    costs = relationship("cost", uselist=False, back_populates="book")
    authors_book  = relationship("author", secondary=regular_books_author, back_populates="publications_books")
    book_categories  = relationship("category", secondary=regular_books_category, back_populates="books")
    __mapper_args__={
        "polymorphic_identity" : "regular_book",
    }
    @staticmethod
    def  getAttributes():
        return {"ISBN":"int","title":"str","publisher":"str","edition":"str","book_shop":"str","cost_id":"int","year_publication":"date","state":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]}
      
class periodics(publication):
    '''implémentation de la classe péeriodics associé au tableau periodics dans la bdd '''
    __tablename__="periodics"

    periodic_id = Column(Integer,ForeignKey("publication.publication_id"),primary_key=True)
    volume = Column(Integer, nullable=False)
    publisher = Column(String(50) , nullable=False)
    edition = Column(String(50),nullable=False)
    book_shop=Column(String(50),nullable=False)
    cost_id = Column(Integer,ForeignKey("cost.cost_id"),nullable=False)
    costs = relationship("cost", uselist=False, back_populates="periodics")
    __mapper_args__={
        "polymorphic_identity" : "periodics",
    }   
    @staticmethod
    def  getAttributes():
        return {"periodic_id":"int","volume":"int","publisher":"str","edition":"str","book_shop":"str","cost_id":"int","year_publication":"date","state":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]} 
    
class internal_reports(publication):
    __tablename__="internal_reports"

    report_id = Column(Integer,ForeignKey("publication.publication_id"),primary_key=True)
    title = Column(String(50),nullable=False)
    __mapper_args__ ={
        "polymorphic_identity" : "internal_reports"
    }   
    
    @staticmethod
    def  getAttributes():
        return {"report_id":"int","title":"str","year_publication":"date","state":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]}   
      
class ECL_thesis(internal_reports):
    __tablename__="ECL_thesis"

    Id_thesis = Column(Integer,ForeignKey("internal_reports.report_id"),primary_key=True)
    Author_id = Column(Integer,nullable=False)
    __mapper_args__ ={
        "polymorphic_identity" : "ECL_thesis"
    } 
    @staticmethod
    def  getAttributes():
        return {"Id_thesis":"int","title":"str","year_publication":"date","state":"restricted_values","Author_id":"int"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]}      
      
class Scientific_Reports(internal_reports):
    __tablename__="Scientific_Reports"

    Id_Report = Column(Integer,ForeignKey("internal_reports.report_id"),primary_key=True)
    authors  = relationship("author", secondary=scientific_author, back_populates="publications")
    __mapper_args__ ={
        "polymorphic_identity" : "Scientific_Reports"
    }   
    @staticmethod
    def  getAttributes():
        return {"Id_Report":"int","title":"str","year_publication":"date","state":"restricted_values"}
    
    '''get the allowed value for the columns with a check constraint'''
    @staticmethod
    def  getRestrictedValue():
        return {"state":["On rack", "issued to","lost","to be bought"]}  
Base.metadata.create_all(engine)
   
    
    