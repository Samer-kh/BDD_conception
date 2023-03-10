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
from services.echange_service import *
class UpdateWindow(QWidget):
    table="Publication"
    tableWidget=None
    Attributes=None
    ValueToAdd=None
    layoutTable=None
    itemNumber=0
    widget=None
    inputs={}
    def __init__(self,table,att,tableWidget,widget):
        super().__init__()
        self.table=table
        self.Attributes=att
        self.tableWidget=tableWidget
        self.widget=widget
        
        '''prepare the layout'''
        
        self.setWindowTitle("Update row")
        Layout=QGridLayout()
        
        ''' adding the adding widgets based of the attribute type
                if the attribute is :
                    int => writing line 
                    string => writing line
                    date => QDateEdit (calender where we can select a date)
                    restrained value ( check constraint) => combo box 
        '''
        self.inputs={}
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
        self.fill()                 
        button_validation=QPushButton("Update row")    
        button_validation.clicked.connect(self.UpdateRow)    
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
            case "Exchange":
                return exchange.getRestrictedValue()            
    ''' fill the spaces with the existing values'''
    def fill(self):
        for i in list(self.inputs.keys()):
            value=getattr(self.widget, self.inputs[i][1])
            match self.inputs[i][0].__class__.__name__:
                case "QLineEdit":
                    self.inputs[i][0].setText (str(value))
                case "QComboBox":
                    self.inputs[i][0].setCurrentText (value)
                case "QDateEdit":
                    value=self.inputs[i][0].setDate(value)
                    
    '''update the row to the database and to the table'''
    
    def UpdateRow(self):
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
                    update_publication(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")
                case "Authers":
                    update_author(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")
                case "Regular Books":
                    update_regular_book(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")
                case "Periodics":
                    update_periodic(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")
                case "Internal Reports":
                    update_internal_reports(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s") 
                case "ECL Thesis":
                    update_ecl_thesis(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")
                case "Scientific_Reports":
                    update_scientific_report(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")  
                case "Cost":
                    update_cost(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s") 
                case "Category":
                    update_cat(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")    
                case "User":
                    update_user(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")   
                case "Lab":
                    update_lab(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s") 
                case "Keyword":
                    update_keyword(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")    
                case "Exchange":
                    update_echange(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectu?? avec succ??s")              
        except:
            self.Error_msg("Echec au niveau de la modification") 
        self.tableWidget.refreshTable()
        self.close()
 
        
    '''afficher un message de succes'''
    
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
        
    '''afficher un message d'erreur'''
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