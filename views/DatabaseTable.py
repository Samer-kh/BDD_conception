from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from services.publication_service import *
from services.author_service import *
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
            
    '''Method to get the table headers'''  
                    
    def getHeaders(self,table):
        match table:
            case "Publication":
                return ["publication_id","year_publication","state"]
            case "Authers":
                return ["author_id","name"]
            case "Regular Books":
                return ["ISBN","title","publisher","edition","book_shop","cost_id","year_publication","state"]
            case "Periodics":
                return ["periodic_id","volume","publisher","edition","book_shop","cost_id","year_publication","state"]
            case "Internal Reports":
                return ["report_id","title","year_publication","state"]
            case "ECL Thesis":
                return ["Id_thesis","title","year_publication","state","Author_id"]
            case "Scientific_Reports":
                return ["Id_Report","title","year_publication","state"]
            case "Cost":
                return ["cost_id","value","currancy"]
            case "currancy":
                return ["Category_id","name_category"]            
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
