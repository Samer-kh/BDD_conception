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

def get_publication(id):
        try:
                return session.get(publication, id)
        except Exception:
                session.rollback()
                raise Exception()
def get_regular_books(id):
        try:
                return session.get(regular_books, id)
        except Exception:
                session.rollback()
                raise Exception()        
def get_periodics(id):
        try:
                return session.get(periodics, id)
        except Exception:
                session.rollback()
                raise Exception()    
def get_internal_reports(id):
        try:
                return session.get(internal_reports, id)
        except Exception:
                session.rollback()
                raise Exception()        
def get_ECL_thesis(id):
        try:
                return session.get(ECL_thesis, id)
        except Exception:
                session.rollback()
                raise Exception()        
def get_scientific_reports(id):
        try:
                return session.get(Scientific_Reports, id)
        except Exception:
                session.rollback()
                raise Exception()
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

def add_publication(state,year_publications,lab_id):
        try:
                pub = publication(state=state,year_publication=year_publications,lab_id=lab_id)
                session.add(pub)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def add_regular_books(state,titles,publishers,editions,year_publications,book_shops,id_cost,lab_id):
        try:
                book = regular_books(state=state,title=titles,publisher=publishers,edition=editions,year_publication=year_publications,
                                book_shop=book_shops,cost_id=id_cost,lab_id=lab_id)
                session.add(book)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
def add_periodics(state,volume,publisher,edition,year_publication,book_shop,id_cost,lab_id):
        try:
                periodic = periodics(state=state,volume=volume,publisher=publisher,edition=edition,year_publication=year_publication,
                                book_shop=book_shop,cost_id=id_cost,lab_id=lab_id)
                session.add(periodic)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
    
def add_internal_reports(state,title,publication_year,lab_id):
        try:
                internal_report = internal_reports(state=state,title=title,year_publication=publication_year,lab_id=lab_id)
                session.add(internal_report)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
def add_ECL_thesis(state,title,authour_id,publication_year,lab_id):
        try:
                ecl_thesis = ECL_thesis(state=state,title=title,year_publication=publication_year,Author_id=authour_id,lab_id=lab_id)
                session.add(ecl_thesis)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
def add_scientific_reports(state,title,publication_year,lab_id):
        try:
                scientific_report = Scientific_Reports(state=state,title=title,year_publication=publication_year,lab_id=lab_id)
                session.add(scientific_report)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
''' services to delete differents documents'''
def delete_publication(id):
        try:
                pub_to_delete = session.get(publication, id)
                session.delete(pub_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
def delete_regular_books(id):
        try:
                book_to_delete = session.get(regular_books, id)
                session.delete(book_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_periodics(id):
        try:
                periodics_to_delete = session.get(periodics, id)
                session.delete(periodics_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
def delete_internal_reports(id):
        try:
                internal_report_to_delete = session.get(internal_reports, id)
                session.delete(internal_report_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()

def delete_ecl_thesiss(id):
        try:
                ecl_thesis_to_delete = session.get(ECL_thesis, id)
                session.delete(ecl_thesis_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
        
def delete_scientific_reports(id):
        try:
                scientific_report_to_delete = session.get(Scientific_Reports, id)
                session.delete(scientific_report_to_delete)
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()


''' services to modify differents documents'''

def update_publication(dict,id):
        try:
                pub_to_update = session.get(publication, id)
                pub_to_update.year_publication = dict["year_publication"]
                pub_to_update.state = dict["state"]        
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()


def update_regular_book(dict,id):
        try:
                book_to_update = session.get(regular_books, id)
                book_to_update.year_publication = dict["year_publication"]
                book_to_update.state = dict["state"]
                book_to_update.ISBN = dict["ISBN"]
                book_to_update.title = dict["title"]
                book_to_update.publisher = dict["publisher"]
                book_to_update.edition = dict["edition"]
                book_to_update.book_shop = dict["book_shop"]
                book_to_update.cost_id = dict["cost_id"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
def update_periodic(dict,id):
        try:
                periodic_to_update = session.get(periodics, id)
                periodic_to_update.year_publication = dict["year_publication"]
                periodic_to_update.state = dict["state"]
                periodic_to_update.ISBN = dict["ISBN"]
                periodic_to_update.volume = dict["volume"]
                periodic_to_update.publisher = dict["publisher"]
                periodic_to_update.edition = dict["edition"]
                periodic_to_update.book_shop = dict["book_shop"]
                periodic_to_update.cost_id = dict["cost_id"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
def update_internal_reports(dict,id):
        try:
                internal_report_to_update = session.get(internal_reports, id)
                internal_report_to_update.year_publication = dict["year_publication"]
                internal_report_to_update.state = dict["state"]   
                internal_report_to_update.title = dict["title"]  
                internal_report_to_update.report_id = dict["report_id"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()
                
def update_ecl_thesis(dict,id):
        try:
                ecl_thesis_to_update = session.get(ECL_thesis, id)
                ecl_thesis_to_update.year_publication = dict["year_publication"]
                ecl_thesis_to_update.state = dict["state"]    
                ecl_thesis_to_update.Id_thesis = dict["Id_thesis"]
                ecl_thesis_to_update.title = dict["title"]  
                ecl_thesis_to_update.Author_id = dict["Author_id"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception() 
                       
def update_scientific_report(dict,id):
        try:
                sc_to_update = session.get(Scientific_Reports, id)
                sc_to_update.year_publication = dict["year_publication"]
                sc_to_update.state = dict["state"] 
                sc_to_update.title = dict["title"]    
                sc_to_update.Id_Report = dict["Id_Report"]
                session.commit()
        except Exception:
                session.rollback()
                raise Exception()