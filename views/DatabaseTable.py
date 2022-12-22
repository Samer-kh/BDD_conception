from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class DatabaseTable(QTableWidget):
    table="Authers"
    def __init__(self,table):
        super().__init__()
        self.table=table  
        
        
        # adding header to the table

        headerH = self.getHeaders(self.table)
        self.setColumnCount(len(headerH))
        headerV = ['a' , 'b' ]
        self.setHorizontalHeaderLabels(headerH)
        self.setVerticalHeaderLabels(headerV)
        header = self.horizontalHeader()  
        for i in range(0,len(headerH),1):     
            header.setSectionResizeMode(i, QHeaderView.Stretch)

        
    def getHeaders(self,table):
        match table:
            case "Publication":
                return ["id","state","year of publication"]
            case "Authers":
                return ["id","name"]

        
