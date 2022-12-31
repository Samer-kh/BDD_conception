from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from services.publication_service import *
from services.author_service import *
from services.category_service import *
from services.cost_service import *
from services.user_service import *
from services.lab_service import *
from services.keyword_service import *
from services.author_scientific_service import *
from services.author_book_service import *
from services.book_category_service import *
from services.keyword_publication import *
from services.keyword_user import *
from services.pub_lab_hascopy import *
from services.user_lab_auth import *
from services.user_lab_notif import *
from services.user_publication_service import *
from services.echange_service import *
import os



class DatabaseTable(QTableWidget):
    table="Publication"
    count=0
    def __init__(self,table):
        super().__init__()
        self.table=table  
        
        '''setting the headers of the table '''
        headerH = self.getHeaders(self.table)
        

        self.setColumnCount(len(headerH))
        #headerV = ['a' , 'b' ]
        
        '''set the table headers'''
        
        self.setHorizontalHeaderLabels(headerH)
        #self.setVerticalHeaderLabels(headerV)
        
        '''stretch the headers to fit all the space'''
        
        header = self.horizontalHeader()  
        for i in range(0,len(headerH),1):     
            header.setSectionResizeMode(i, QHeaderView.Stretch)
            
        '''setting the rows of the table'''
        
        rows=self.getTableRows(self.table)
        self.setRowCount(len(rows))
        for i in rows:
            for att in range(0,len(headerH)):
                self.setItem(self.count, att, QTableWidgetItem(str(getattr(i,headerH[att]))))
            self.count += 1
        
        '''application of the delegate '''
            
        delegate = StyledItemDelegate(self)
        self.setItemDelegate(delegate) 
        
    '''method to get the table rows '''
           
    def getTableRows(self,table):
        match table:
            case "Publication":
                return get_publication_all()
            case "Authers":
                return get_all_authors() 
            case "Regular Books":
                return get_regular_books_all()
            case "Periodics":
                return get_periodics_all()
            case "Internal Reports":
                return get_internal_reports_all()
            case "ECL Thesis":
                return get_ECL_thesis_all()
            case "Scientific_Reports":
                return get_scientific_reports_all()   
            case "Cost":
                return get_all_costs() 
            case "Category":
                return get_all_cat()      
            case "User":
                return get_all_users()  
            case "Lab":
                return get_all_labs()
            case "Keyword":
                return get_all_keywords()  
            case "Exchange":
                return get_all_exchange()              
            case "Relation scientific reports and authors":
                return get_all_auth_sci()
            case "Relation regular books and authers":
                return get_all_auth_book()
            case "Relation regular books and Categories" :
                return get_all_cat_book()
            case "Relation user and publication":
                return get_all_user_pub()
            case "Relation user and lab - authentification":
                return get_all_user_lab_auth()
            case "Relation user and lab - Notify": 
                return get_all_user_lab_notif()
            case "Relation publication and lab - has copy":
                return get_all_pub_lab_hascopy()
            case "Relation keyword and user":
                return get_all_key_user()
            case "Relation Keyword and publication": 
                return get_all_key_pub()   
    '''Method to get the table headers'''  
                    
    def getHeaders(self,table):
        match table:
            case "Publication":
                return ["publication_id","year_publication","state","lab_id"]
            case "Authers":
                return ["author_id","name"]
            case "Regular Books":
                return ["ISBN","title","publisher","edition","book_shop","cost_id","year_publication","state","lab_id"]
            case "Periodics":
                return ["periodic_id","volume","publisher","edition","book_shop","cost_id","year_publication","state","lab_id"]
            case "Internal Reports":
                return ["report_id","title","year_publication","state","lab_id"]
            case "ECL Thesis":
                return ["Id_thesis","title","year_publication","state","Author_id","lab_id"]
            case "Scientific_Reports":
                return ["Id_Report","title","year_publication","state","lab_id"]
            case "Cost":
                return ["cost_id","value","currancy","id_echange"]
            case "Category":
                return ["Category_id","name_category"]   
            case "User":
                return ["user_id","email"]   
            case "Lab":
                return ["lab_id","lab_name"]   
            case "Keyword":
                return ["key_id","value"]  
            case "Exchange":
                return ["exchange_id","euro_to_dollar","pound_to_dollar","pound_to_dollar"]
            
            case "Relation scientific reports and authors":
                return ["id","author_id","Id_Report"]
            case "Relation regular books and authers":
                return ["id","author_id","ISBN"]
            case "Relation regular books and Categories" :
                return ["id","ISBN","Category_id"]
            case "Relation user and publication":
                return ["id","user_id","publication_id"]
            case "Relation user and lab - authentification":
                return ["id","user_id","lab_id"]
            case "Relation user and lab - Notify": 
                return ["id","user_id","lab_id"]
            case "Relation publication and lab - has copy":
                return ["id","publication_id","lab_id"]
            case "Relation keyword and user":
                return ["id","key_id","user_id"]
            case "Relation Keyword and publication": 
                return ["id","key_id","publication_id"]   
                  
    ''' refresh table after doing an operation'''        
    def refreshTable(self):
        self.setRowCount(0)
        headerH = self.getHeaders(self.table)
        rows=self.getTableRows(self.table)
        self.setRowCount(len(rows))
        self.count=0
        for i in rows:
            for att in range(0,len(headerH)):
                self.setItem(self.count, att, QTableWidgetItem(str(getattr(i,headerH[att]))))
            self.count += 1


'''a delegate to render table cells non-editable'''

class StyledItemDelegate(QStyledItemDelegate):
    def createEditor(self, *args):
        editor = super().createEditor(*args)
        if isinstance(editor, QLineEdit):
            editor.setReadOnly(True)
        return editor        
