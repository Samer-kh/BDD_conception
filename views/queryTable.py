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
import os



class QueryTable(QTableWidget):
    keys=[]
    rows=[]
    count=0
    def __init__(self,rows,keys):
        super().__init__() 
        self.keys=keys
        self.rows=rows
        '''setting the headers of the table '''
        
        headerH = self.keys
        

        self.setColumnCount(len(headerH))
        
        '''set the table headers'''
        
        self.setHorizontalHeaderLabels(headerH)
        #self.setVerticalHeaderLabels(headerV)
        
        '''stretch the headers to fit all the space'''
        
        header = self.horizontalHeader()  
        for i in range(0,len(headerH),1):     
            header.setSectionResizeMode(i, QHeaderView.Stretch)
            
        '''setting the rows of the table'''
        
        self.setRowCount(len(self.rows))
        for i in self.rows:
            print(i)
            for att in range(0,len(headerH)):
                self.setItem(self.count, att, QTableWidgetItem(str(i[att])))
            self.count += 1
        
        '''application of the delegate '''
            
        delegate = StyledItemDelegate(self)
        self.setItemDelegate(delegate) 
        
    
                  
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
