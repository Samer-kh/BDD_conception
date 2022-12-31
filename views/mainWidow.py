import sys
import re 
import functools
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from views.CheckableComboBox import *
from views.DatabaseTable import *
from views.AddWindow import *
from views.DeleteWindow import *
from views.PreUpdateWindow import *
from persistance.cost import *
from persistance.category import *
from views.SpecialAdd import *
from persistance.Lab import *
from persistance.keyword import *

class GraphicalInterface(QMainWindow):
    Buttons=[]
    Table_box=None
    widget=None
    tableSet=False
    addWidow=None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Graphical Interface")
        '''layout initialization'''
        self.Stacked_layout=QStackedLayout()
        Page_layout=QVBoxLayout()
        Button_layout=QHBoxLayout()
        
        '''adding layouts '''
        
        Page_layout.addLayout(Button_layout)
        Page_layout.addLayout(self.Stacked_layout)
        
        '''button configuration'''
        
        button_add=QPushButton("Add a row")
        button_delete=QPushButton("Delete a row")
        button_update=QPushButton("Update a row")
        self.Table_box=QComboBox()
        button_change=QPushButton("Change table")
        Logo=QLabel()
        button_special=QPushButton("Special Queries")
        '''add the buttons to the list for save later'''
        
        self.Buttons.append(button_add)
        self.Buttons.append(button_delete)
        self.Buttons.append(button_update)
        self.Buttons.append(Logo) 
        self.Buttons.append(button_change)    
        self.Buttons.append(self.Table_box)  
        self.Buttons.append(button_special) 
        '''preparing icons'''
        
        pixmap=QPixmap("./images/ecl.png")
        Logo.setPixmap(pixmap)
        
        pixmapi_add = getattr(QStyle, "SP_DialogSaveButton")
        pixmapi_delete = getattr(QStyle, "SP_DialogDiscardButton")
        pixmapi_update = getattr(QStyle , 'SP_DialogResetButton')
        pixmapi_changed = getattr(QStyle , 'SP_DialogApplyButton')
        pixmapi_special = getattr(QStyle , 'SP_FileDialogContentsView')
        
        icon_delete = self.style().standardIcon(pixmapi_delete)
        icon_add = self.style().standardIcon(pixmapi_add)
        icon_update = self.style().standardIcon(pixmapi_update)
        icon_change = self.style().standardIcon(pixmapi_changed)
        icon_special = self.style().standardIcon(pixmapi_special)
        
        '''adding icons to buttons'''
        
        button_add.setIcon(icon_add)
        button_delete.setIcon(icon_delete)
        button_update.setIcon(icon_update)
        button_change.setIcon(icon_change)
        button_special.setIcon(icon_special)
        '''setting buttons height'''
        
        button_add.setFixedHeight(50)
        button_delete.setFixedHeight(50)
        button_update.setFixedHeight(50)
        Logo.setFixedHeight(50)
        self.Table_box.setFixedHeight(50)
        button_change.setFixedHeight(50)
        button_special.setFixedHeight(50)
        '''setting the size policy'''
        
        button_add.setSizePolicy(
        QSizePolicy.Preferred,
        QSizePolicy.Preferred)
        
        '''ajouter les noms des tableaux au box'''
        
        self.setTableNames(self.Table_box)
        
        
        ''' event control of the different parts of the layout'''
        button_change.clicked.connect(self.addTable)
        button_add.clicked.connect(self.openAdditionTab)
        button_delete.clicked.connect(self.openDeleteTab)
        button_update.clicked.connect(self.openUpdateTab)
        button_special.clicked.connect(self.getSpecialQueries)
        '''add the buttons to the widget'''
        
        Button_layout.addWidget(button_add,Qt.AlignRight)
        Button_layout.addWidget(button_update,Qt.AlignRight)
        Button_layout.addWidget(button_delete,Qt.AlignRight)
        Button_layout.addWidget(self.Table_box,Qt.AlignCenter)
        Button_layout.addWidget(button_change,Qt.AlignLeft)
        Button_layout.addWidget(button_special,Qt.AlignLeft)
        Button_layout.addWidget(Logo,Qt.AlignLeft)
        
        

        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        
        '''setting the layout and the widget of the main window'''
        
        widget=QWidget()
        widget.setLayout(Page_layout)
        self.setCentralWidget(widget)
        
        '''add the table to the layout'''
        
        self.addTable()
            

    '''Manage the table names '''       
    def setTableNames(self,box):
        box.addItems(["Publication","Authers","Regular Books","Periodics","Internal Reports","ECL Thesis","Scientific_Reports","Cost","Category","User","Lab","Keyword","Exchange",
                      "Relation scientific reports and authors" , "Relation regular books and authers", "Relation regular books and Categories" ,"Relation user and publication",
                      "Relation user and lab - authentification","Relation user and lab - Notify" , "Relation publication and lab - has copy",
                      "Relation keyword and user","Relation Keyword and publication"])
    
    '''show the chosen table'''
        
    def addTable(self):
        table= self.Table_box.currentText()
        if self.tableSet==False:
            self.widget=DatabaseTable(table)
            self.Stacked_layout.addWidget(self.widget)
            self.tableSet=True
        else:
            self.Stacked_layout.itemAt(0).widget().setParent(None)
            self.widget=DatabaseTable(table)
            self.Stacked_layout.addWidget(self.widget)
        if (table in ["Publication","Authers","Regular Books","Periodics","Internal Reports","ECL Thesis","Scientific_Reports","Cost","Category","User","Lab","Keyword","Exchange"]):
            self.Buttons[0].setEnabled(True)
            self.Buttons[1].setEnabled(True)
            self.Buttons[2].setEnabled(True)  
        else:
            self.Buttons[1].setEnabled(False)
            self.Buttons[2].setEnabled(False)    
            
    def openAdditionTab(self):
        global addWindow
        table= self.Table_box.currentText()
        att=self.getAttributesFromTable()
        addWindow=AddWindow(table,att,self.widget,self.Stacked_layout)
        self.addWidow=addWindow      
        addWindow.show()   
        
    def openDeleteTab(self):
        global deleteWindow
        table= self.Table_box.currentText()
        att=self.getAttributesFromTable()
        deleteWindow=DeleteWindow(table,att,self.widget)
        self.deleteWindow=deleteWindow      
        deleteWindow.show()     

    def openUpdateTab(self):
        global preUpdateWindow
        table= self.Table_box.currentText()
        att=self.getAttributesFromTable()
        preUpdateWindow=PreUpdateWindow(table,att,self.widget)
        self.preUpdateWindow=preUpdateWindow      
        preUpdateWindow.show()    
    '''Get the attributes from the table '''
        
    def getAttributesFromTable(self):   
        match self.Table_box.currentText():
            case "Publication":
                return publication.getAttributes()
            case "Authers":
                return author.getAttributes()
            case "Regular Books":
                return regular_books.getAttributes()
            case "Periodics":
                return periodics.getAttributes()
            case "Internal Reports":
                return internal_reports.getAttributes()
            case "ECL Thesis":
                return ECL_thesis.getAttributes()
            case "Scientific_Reports":
                return Scientific_Reports.getAttributes()
            case "Cost":
                return cost.getAttributes()
            case "Category":
                return category.getAttributes()            
            case "User":
                return user.getAttributes() 
            case "Lab":
                return lab.getAttributes() 
            case "Keyword":
                return keyword.getAttributes()   
            case 'Exchange':
                return exchange.getAttributes()   
            case "Relation scientific reports and authors":
                return {"id":"int","author_id":"int","Id_Report":"int"}
            case "Relation regular books and authers":
                return {"id":"int","author_id":"int","ISBN":"int"}
            case "Relation regular books and Categories" :
                return {"id":"int","ISBN":"int","Category_id":"int"}
            case "Relation user and publication":
                return {"id":"int","user_id":"int","publication_id":"int"}
            case "Relation user and lab - authentification":
                return {"id":"int","user_id":"int","lab_id":"int"}
            case "Relation user and lab - Notify": 
                return {"id":"int","user_id":"int","lab_id":"int"}
            case "Relation publication and lab - has copy":
                return {"id":"int","publication_id":"int","lab_id":"int"}
            case "Relation keyword and user":
                return {"id":"int","key_id":"int","user_id":"int"}
            case "Relation Keyword and publication": 
                return {"id":"int","key_id":"int","publication_id":"int"}         
    def getSpecialQueries(self):
        global queryWindow
        queryWindow=SpecialAdd(self,self.Buttons)     
        queryWindow.show()
if __name__=="__main__":
    app=QApplication(sys.argv)
    
    ''' setting the style '''
    
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    
    widget=GraphicalInterface()
    widget.resize(1000,1000)
    widget.show()
    app.exec_()
    sys.exit()