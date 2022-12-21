from persistance.author import *
from persistance.inter_tables import *
from persistance.publication import *

def add_books_to_authors(id_book,id_author):
    book_to_add = session.get(regular_books, id_book)
    author_effected = session.get(author, id_author)
    author_effected.publications_books.append(book_to_add)
    
    session.add(author_effected)
    session.commit()
    
def add_author_to_books(id_book,id_author):
    book_effected = session.get(regular_books, id_book)
    author_to_add = session.get(author, id_author)
    book_effected.authors_book.append(author_to_add)
    
    session.add(book_effected)
    session.commit()   