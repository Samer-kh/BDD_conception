from sqlalchemy import Column,  ForeignKey, Integer, String , Float ,Date , Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,  relationship



''' defining the tables using sqlAlchemy'''

engine = create_engine("mysql://root:@localhost/bibliotheque")
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()
Base.metadata.bind = engine

''' 
    creating the middle table for the implementation of the n:n relation 
    between the author and the scientific reports 
'''
# Table intermédiaire
scientific_author = Table(
 "scientific_author",
 Base.metadata,
 Column("id", Integer, primary_key=True),
 Column("author_id", ForeignKey("author.author_id")),
 Column("Id_Report", ForeignKey("Scientific_Reports.Id_Report")),
)

regular_books_author = Table(
 "regular_books_author",
 Base.metadata,
 Column("id", Integer, primary_key=True),
 Column("author_id", ForeignKey("author.author_id")),
 Column("ISBN", ForeignKey("regularbooks.ISBN")),
)

regular_books_category = Table(
 "regular_books_category",
 Base.metadata,
 Column("id", Integer, primary_key=True),
 Column("author_id", ForeignKey("regularbooks.ISBN")),
 Column("Category_id", ForeignKey("categories.Category_id")),
)

user_publication = Table(
 "user_publication",
 Base.metadata,
 Column("id", Integer, primary_key=True),
 Column("user_id", ForeignKey("user.user_id")),
 Column("publication_id", ForeignKey("publication.publication_id")),
)