from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
from services.publication_service import *
from services.author_service import *
from views.UpdateWindow import *
class PreUpdateWindow(QWidget):
    table="Publication"
    input=None
    def __init__(self,table,att,tableWidget):
        super().__init__()
        self.table=table
        self.Attributes=att
        self.tableWidget=tableWidget

        
        '''prepare the layout'''
        
        self.setWindowTitle("specify row ID for update ")
        Layout=QGridLayout()
        
        ''' adding the updating widgets based of the attribute type
                if the attribute is :
                    id => writing line 
        '''
        id=list(self.Attributes.keys())[0]
        label_add=QLabel(id+' :')
        self.input=QLineEdit()
        Layout.addWidget(label_add,0,0,1,2)
        Layout.addWidget(self.input,0,2,1,4)

                    
        button_validation=QPushButton("select row to update")    
        button_validation.clicked.connect(self.rowSelection)    
        Layout.addWidget(button_validation,1,0,1,6)  
                                          
        ''' add the layout to the widget '''   
        
        self.setLayout(Layout)
        
        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        
    def rowSelection(self):
        value=self.input.text()
        global updateWindow
        match self.table:
            case "Publication":
                publication=get_publication(value)                
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,publication)
                self.updateWindow=updateWindow      
                updateWindow.show() 
                self.close()
            case "Authers":
                author=get_authors(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,author)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close() 
            case "Regular Books":
                book=get_regular_books(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,book)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close() 
            case "Periodics":
                periodic=get_periodics(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,periodic)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close()
            case "Internal Reports":
                internal=get_internal_reports(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,internal)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close()
            case "ECL Thesis":
                ecl_thesis=get_ECL_thesis(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,ecl_thesis)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close()
            case "Scientific_Reports":
                rep=get_scientific_reports(value)
                updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,rep)
                self.updateWindow=updateWindow      
                updateWindow.show()
                self.close()
        self.tableWidget.refreshTable()