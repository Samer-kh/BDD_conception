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
from views.AmountAndCat import *
from views.YearAndAuth import *
from views.getPublisher import *
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
        self.listQueries.addItem("Query One ")
        self.listQueries.addItem("Query Two ")
        self.listQueries.addItem("Query Three ")
        self.listQueries.addItem("Query Four ")
        self.listQueries.addItem("Query Five ")
        self.listQueries.addItem("Query Six ")
        self.listQueries.addItem("Query Seven ")
        self.listQueries.addItem("Query Eight ")
        self.listQueries.addItem("Query Nine ")
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
                 QMessageBox.information(self, "Query Three", '''For a given user, evaluate whether (s)he can borrow a particular publication at a given
time. (will depend on the availability status and the accessrights''')
         
            case 4:
                     QMessageBox.information(self, "Query six", '''if there is a publication such that a particular user has rights to borrow it (a copy), but it
is (all copies for which the user has rights are) issued to some one else then show the
email address(es) of all those users who presently have a borrowed copy of the
publication that this user has also right to borrow''')
            
                
            case 5:
                  QMessageBox.information(self, "Query six", " List all publication belonging to a particular category, and costing less than a particular amount.")
            case 6:
                QMessageBox.information(self, "Query six", "  List all publications authored by a particular author, and published after a particular year")
         
            case 7:
                QMessageBox.information(self, "Query six", "  For a given publisher, prepare a list of “books published” chronologically ")
         
                 
            case 8 :
                QMessageBox.information(self, "Query six", "  List all lost regular books (title, publisher, ISBN) along with owner and price, sorting them according to owner, and then ISBN. ")
         
        
        
      
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
                global getAmountAndCat
                getAmountAndCat=AmountAndCat(self.mainWidget,self.Buttons)
                getAmountAndCat.show() 
            case 6:
                global getYearandAuth
                getYearandAuth=YearAndAuth(self.mainWidget,self.Buttons)
                getYearandAuth.show() 
            case 7:
                global getPublishers
                getPublishers=GetPublisher(self.mainWidget,self.Buttons)
                getPublishers.show() 
            case 8 : 
                (rows,keys)=execute_query_nine()
                newTable=QueryTable(rows,keys)
                self.mainWidget.Stacked_layout.itemAt(0).widget().setParent(None)
                self.mainWidget.widget=newTable
                self.mainWidget.Stacked_layout.addWidget(self.mainWidget.widget)
                self.Buttons[0].setEnabled(False)
                self.Buttons[1].setEnabled(False)
                self.Buttons[2].setEnabled(False)
        
        
        
class myListWidget(QListWidget):

   def Clicked(self,item):
      QMessageBox.information(self, "ListWidget", "You clicked: "+item.text())