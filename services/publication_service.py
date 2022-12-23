''' this file contains the functions that handle all the operationrelated to the publications 
    Operations supported : 
        add , modify , delete

'''
from  persistance.publication import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

''' services to fetch the different documents by id'''
def get_publication_all():
        return session.query(publication).all()

def get_regular_books(id):
        return session.get(regular_books, id)
        
def get_periodics(id):
        return session.get(periodics, id)
    
def get_internal_reports(id):
        return session.get(internal_reports, id)
        
def get_ECL_thesis(id):
        return session.get(ECL_thesis, id)
        
def get_scientific_reports(id):
        return session.get(Scientific_Reports, id)

''' fetch all documents'''

def get_regular_books_all():
        return session.query(regular_books).all()
        
def get_periodics_all():
        return session.query(periodics).all()
    
def get_internal_reports_all():
        return session.query(internal_reports).all()
        
def get_ECL_thesis_all():
        return session.query(ECL_thesis).all()
        
def get_scientific_reports_all():
        return session.query(Scientific_Reports).all()

''' services to add the different documents '''

def add_regular_books(state,titles,publishers,editions,year_publications,book_shops,id_cost):
        book = regular_books(state=state,title=titles,publisher=publishers,edition=editions,year_publication=year_publications,
                            book_shop=book_shops,cost_id=id_cost)
        session.add(book)
        session.commit()
        
def add_periodics(state,volume,publisher,edition,year_publication,book_shop,id_cost):
        periodic = periodics(state=state,volume=volume,publisher=publisher,edition=edition,year_publication=year_publication,
                            book_shop=book_shop,cost_id=id_cost)
        session.add(periodic)
        session.commit()
    
def add_internal_reports(state,title,publication_year):
        internal_report = internal_reports(state=state,title=title,year_publication=publication_year)
        session.add(internal_report)
        session.commit()
        
def add_ECL_thesis(state,title,authour_id,publication_year):
        ecl_thesis = ECL_thesis(state=state,title=title,year_publication=publication_year,Author_id=authour_id)
        session.add(ecl_thesis)
        session.commit()
        
def add_scientific_reports(state,title,publication_year):
        scientific_report = Scientific_Reports(state=state,title=title,year_publication=publication_year)
        session.add(scientific_report)
        session.commit()
        
''' services to delete differents documents'''

def delete_regular_books(id):
        book_to_delete = session.get(regular_books, id)
        session.delete(book_to_delete)
        session.commit()

def delete_periodics(id):
        periodics_to_delete = session.get(periodics, id)
        session.delete(periodics_to_delete)
        session.commit()
        
def delete_internal_reports(id):
        internal_report_to_delete = session.get(internal_reports, id)
        session.delete(internal_report_to_delete)
        session.commit()

def delete_ecl_thesiss(id):
        ecl_thesis_to_delete = session.get(ECL_thesis, id)
        session.delete(ecl_thesis_to_delete)
        session.commit()
        
def delete_scientific_reports(id):
        scientific_report_to_delete = session.get(Scientific_Reports, id)
        session.delete(scientific_report_to_delete)
        session.commit()

''' services to modify differents documents'''

def update_regular_book(dict,id):
    book_to_update = session.get(regular_books, id)
    for i in list(dict.keys()):
        book_to_update.i = dict[i]
        session.commit()

def update_periodic(dict,id):
    periodic_to_update = session.get(periodics, id)
    for i in list(dict.keys()):
        periodic_to_update.i = dict[i]
        session.commit()

def update_internal_reports(dict,id):
    internal_report_to_update = session.get(periodics, id)
    for i in list(dict.keys()):
        internal_report_to_update.i = dict[i]
        session.commit()