from persistance.category import *
from persistance.inter_tables import *
from persistance.publication import *


def add_book_to_category(id_book,id_category):
    book_to_add = session.get(regular_books, id_book)
    category_effected = session.get(category, id_category)
    category_effected.books.append(book_to_add)
    
    session.add(category_effected)
    session.commit()
    
def add_category_to_book(id_book,id_category):
    book_effected = session.get(regular_books, id_book)
    category_to_add = session.get(category, id_category)
    book_effected.book_categories.append(category_to_add)
    session.add(book_effected)
    session.commit()   
    
def get_all_cat_book():
    return session.query(regular_books_category).all()  