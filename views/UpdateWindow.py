from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
from services.publication_service import *
from services.author_service import *
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
        for i in list(self.Attributes.keys()):
            match self.Attributes[i]:
                case "int":
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
    ''' fill the spaces with the existing values'''
    def fill(self):
        for i in list(self.inputs.keys()):
            value=getattr(self.widget, self.inputs[i][1])
            match self.inputs[i][0].__class__.__name__:
                case "QLineEdit":
                    print("QLine")
                    self.inputs[i][0].setText (str(value))
                case "QComboBox":
                    print("QComboBox")
                    self.inputs[i][0].setCurrentText (value)
                case "QDateEdit":
                    print("QDateEdit")
                    value=self.inputs[i][0].setDate(value)
                    
    '''update the row to the database and to the table'''
    
    def UpdateRow(self):
        count=0
        valueDict={}
        for i in list(self.inputs.keys()):
            match self.inputs[i][0].__class__.__name__:
                case "QLineEdit":
                    print("QLine")
                    value=self.inputs[i][0].text()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value
                case "QComboBox":
                    print("QComboBox")
                    value=self.inputs[i][0].currentText()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value
                case "QDateEdit":
                    print("QDateEdit")
                    value=self.inputs[i][0].date()
                    row=self.tableWidget.rowCount()+1
                    valueDict[self.inputs[i][1]]=value.toPython()
            count+=1
            print(valueDict)
        try:
            match self.table:
                case "Publication":
                    update_publication(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectué avec succés")
                case "Authers":
                    update_author(valueDict,valueDict[list(valueDict.keys())[0]])
                    self.Success_msg("Modification effectué avec succés")
        except:
            self.Error_msg("Echec au niveau de la modification")
        print(valueDict)  
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
        msg.setText("Succès:")
        msg.setInformativeText(txt)
        msg.setWindowTitle("Message de Succès")
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