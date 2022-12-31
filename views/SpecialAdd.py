from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
from services.publication_service import *
from services.author_service import *
from services.category_service import *
from services.cost_service import *
from services.user_service import *
from services.queries_service import *
from views.queryTable import *
from views.getUserandLab import *
from views.getLab import *
class SpecialAdd(QWidget):
    table="Publication"
    mainWidget=None
    Buttons=None
    def __init__(self,widget,Buttons):
        super().__init__()
        self.mainWidget=widget
        self.Buttons=Buttons
        '''prepare the layout'''
        
        self.setWindowTitle("Special Queries available")
        Layout=QGridLayout()
        
        '''Prepare the list'''
        self.listQueries=myListWidget()
        self.listQueries.addItem("All the publications registered in the library system")
        self.listQueries.addItem("Publications issued to a user and owned by any lab ")
        self.listQueries.addItem("Price of all publications owned")
        self.listQueries.addItem("evaluatation")
        self.listQueries.addItem("Users with a borrowed copy")
        self.listQueries.addItem("Publications authored by a particular author")
        self.listQueries.addItem("list of “books published”")
        self.listQueries.addItem("lost regular books ")
        self.listQueries.itemDoubleClicked.connect(self.Clicked)
        
        
        
        Layout.addWidget(self.listQueries,0,0,25,6) 
        
        Button=QPushButton("Execute")
        Button.clicked.connect(self.queryActivation)
        Layout.addWidget(Button,25,0,3,6) 
        '''set the layout'''
        
        self.setLayout(Layout)
        
        self.resize(700,400)
        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
    def Clicked(self,item):
        row = self.listQueries.currentRow()
        match row:
            case 0:
                QMessageBox.information(self, "Query one", "List all the publications registered in the library system (Do not show duplicates owned by different labs)")
            case 1:
                QMessageBox.information(self, "Query Two", "For a given user, list all the publications issued to her/him and owned by any lab/ a particular lab")
            case 2:
                QMessageBox.information(self, "Query Three", "Evaluate the price of all publications owned by a particular lab in €. (at the running rate of other currencies)")
         
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
        
        
      
    def queryActivation(self):
        row = self.listQueries.currentRow()
        match row:
            case 0:
                (rows,keys)=execute_query_one()
                newTable=QueryTable(rows,keys)
                self.mainWidget.Stacked_layout.itemAt(0).widget().setParent(None)
                self.mainWidget.widget=newTable
                self.mainWidget.Stacked_layout.addWidget(self.mainWidget.widget)
                self.Buttons[0].setEnabled(False)
                self.Buttons[1].setEnabled(False)
                self.Buttons[2].setEnabled(False)
            case 1:
                global getUserAndLab
                getUserAndLab=GetUserAndLab(self.mainWidget,self.Buttons)
                getUserAndLab.show() 
            case 2:
                global getLab
                getLab=GetLab(self.mainWidget,self.Buttons)
                getLab.show() 
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
        
        
        
class myListWidget(QListWidget):

   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())