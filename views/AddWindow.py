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

class AddWindow(QWidget):
    table="Publication"
    tableWidget=None
    Attributes=None
    ValueToAdd=None
    layoutTable=None
    itemNumber=0
    inputs={}
    def __init__(self,table,att,tableWidget,layoutTable):
        super().__init__()
        self.table=table
        self.Attributes=att
        self.tableWidget=tableWidget
        self.layoutTable=layoutTable
        self.inputs={}
        '''prepare the layout'''
        
        self.setWindowTitle("add row")
        Layout=QGridLayout()
        
        ''' adding the adding widgets based of the attribute type
                if the attribute is :
                    int => writing line 
                    string => writing line
                    date => QDateEdit (calender where we can select a date)
                    restrained value ( check constraint) => combo box 
        '''
        for i in list(self.Attributes.keys()):
            match self.Attributes[i]:
                case "int":
                    label_add=QLabel(i+' :')
                    input=QLineEdit()
                    self.inputs[i]=(input,i)
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1
                case "float":
                    label_add=QLabel(i+' :')
                    input=QLineEdit()
                    self.inputs[i]=(input,i)
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1
                case "str":
                    label_add=QLabel(i+' :')
                    input=QLineEdit()
                    self.inputs[i]=(input,i)
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1    
                case "date":
                    label_add=QLabel(i+' :')
                    input = QDateEdit(calendarPopup=True)
                    input.setDateTime(QDateTime.currentDateTime())
                    self.inputs[i]=(input,i)
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1  
                case "restricted_values":
                    label_add=QLabel(i+' :')
                    input = QComboBox()
                    input.addItems(self.getRestricted()[i])
                    self.inputs[i]=(input,i)
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)  
                    self.itemNumber+=1                    
        button_validation=QPushButton("Add row")    
        button_validation.clicked.connect(self.addRow)    
        Layout.addWidget(button_validation,self.itemNumber,0,1,6)  
                                          
        ''' add the layout to the widget '''   
        
        self.setLayout(Layout)
        
        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
    
    def getRestricted(self):
        match self.table:
            case "Publication":
                return publication.getRestrictedValue()
            case "Authers":
                return author.getRestrictedValue()  
            case "Regular Books":
                return regular_books.getRestrictedValue() 
            case "Periodics":
                return periodics.getRestrictedValue() 
            case "Internal Reports":
                return internal_reports.getRestrictedValue() 
            case "ECL Thesis":
                return ECL_thesis.getRestrictedValue() 
            case "Scientific_Reports":
                return Scientific_Reports.getRestrictedValue()    
            case "Cost":
                return cost.getRestrictedValue()  
            case "Category":
                return category.getRestrictedValue()   
            case "User":
                return user.getRestrictedValue()   
            case "Lab":
                return lab.getRestrictedValue() 
            case "Keyword":
                return keyword.getRestrictedValue()
            case other:
                return {}              
    '''add the row to the database and to the table'''
    
    def addRow(self):
        count=0
        valueDict={}
        for i in list(self.inputs.keys()):
            match self.inputs[i][0].__class__.__name__:
                case "QLineEdit":
                    value=self.inputs[i][0].text()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value
                case "QComboBox":
                    value=self.inputs[i][0].currentText()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value
                case "QDateEdit":
                    value=self.inputs[i][0].date()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value.toPython()
            count+=1
        try:
            match self.table:
                case "Publication":
                    add_publication(valueDict["state"],valueDict["year_publication"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "Authers":
                    add_authors(valueDict["name"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "Regular Books":
                    add_regular_books(valueDict["state"],valueDict["title"],valueDict["publisher"],valueDict["edition"]
                          ,valueDict["year_publication"],valueDict["book_shop"],valueDict["cost_id"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                case "Periodics":
                    add_periodics(valueDict["state"],valueDict["volume"],valueDict["publisher"],valueDict["edition"]
                          ,valueDict["year_publication"],valueDict["book_shop"],valueDict["cost_id"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                case "Internal Reports":
                    add_internal_reports(valueDict["state"],valueDict["title"],valueDict["year_publication"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "ECL Thesis":
                    add_ECL_thesis(valueDict["state"],valueDict["title"],valueDict["Author_id"],valueDict["year_publication"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                case "Scientific_Reports":
                    add_scientific_reports(valueDict["state"],valueDict["title"],valueDict["year_publication"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "Cost":
                    add_cost(valueDict["value"],valueDict["currancy"],valueDict["id_echange"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "Exchange":
                    add_echange(valueDict["euro_to_dollar"],valueDict["pound_to_dollar"],valueDict["euro_to_pound"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                case "Category":
                    add_cat(valueDict["name_category"])
                    self.Success_msg("ligne ajout??e avec succ??s")      
                case "User":
                    add_user(valueDict["email"])
                    self.Success_msg("ligne ajout??e avec succ??s")  
                case "Lab":
                    add_lab(valueDict["lab_name"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                case "Keyword":
                    add_keyword(valueDict["value"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation scientific reports and authors":
                    add_author_to_scientifics(valueDict["Id_Report"],valueDict["author_id"])
                    add_scientific_to_authors(valueDict["Id_Report"],valueDict["author_id"])
                    add_keyword(valueDict["value"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation regular books and authers":
                    add_author_to_books(valueDict["ISBN"],valueDict["author_id"])
                    add_books_to_authors(valueDict["ISBN"],valueDict["author_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation regular books and Categories" :
                    print(valueDict)
                    add_book_to_category((valueDict["ISBN"],valueDict["Category_id"]))
                    add_category_to_book((valueDict["ISBN"],valueDict["Category_id"]))
                    self.Success_msg("ligne ajout??e avec succ??s") 

                case "Relation user and publication":
                    add_user_to_publication(valueDict["publication_id"],valueDict["user_id"])
                    add_publication_to_users(valueDict["publication_id"],valueDict["user_id"])
                    self.Success_msg("ligne ajout??e avec succ??s")
                    
                case "Relation user and lab - authentification":
                    add_user_to_lab(valueDict["lab_id"],valueDict["user_id"])
                    add_Lab_to_users(valueDict["lab_id"],valueDict["user_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation user and lab - Notify": 
                    add_Lab_to_users_notif(valueDict["lab_id"],valueDict["user_id"])
                    add_user_to_lab_notif(valueDict["lab_id"],valueDict["user_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation publication and lab - has copy":
                    add_pub_to_lab(valueDict["publication_id"],valueDict["lab_id"])
                    add_lab_to_pub(valueDict["publication_id"],valueDict["lab_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation keyword and user":
                    add_key_to_users_(valueDict["key_id"],valueDict["user_id"])
                    add_user_to_key(valueDict["key_id"],valueDict["user_id"])
                    self.Success_msg("ligne ajout??e avec succ??s") 
                    
                case "Relation Keyword and publication": 
                    add_pub_to_key(valueDict["key_id"],valueDict["publication_id"])
                    add_key_to_pub(valueDict["key_id"],valueDict["publication_id"])
                    self.Success_msg("ligne ajout??e avec succ??s")  
                                                     
        except Exception :
            self.close()
            self.Error_msg("Merci de verifier les contraintes d'ajout et les types des variables")      
        self.tableWidget.refreshTable()
        self.close()
    def Success_msg(self,txt):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        msg = QMessageBox(self)
        #msg.setStyleSheet("QMessageBox{width: 1000px;}");
        msg.setIcon(QMessageBox.Information)
        msg.setText("Succ??s:")
        msg.setInformativeText(txt)
        msg.setWindowTitle("Message de Succ??s")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setTextFormat(Qt.RichText)
        msg.resize(msg.sizeHint())
        msg.exec_()
    def Error_msg(self,txt):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        msg = QMessageBox(self)
        msg.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erreur :")
        msg.setInformativeText(txt)
        msg.setWindowTitle("Message d'erreur")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()