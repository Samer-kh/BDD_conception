from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
class AddWindow(QWidget):
    table="Publication"
    tableWidget=None
    Attributes=None
    ValueToAdd=None
    itemNumber=0
    inputs={}
    def __init__(self,table,att,tableWidget):
        super().__init__()
        self.table=table
        self.Attributes=att
        self.tableWidget=tableWidget
        
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
                    self.inputs[i]=input
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1
                case "str":
                    label_add=QLabel(i+' :')
                    input=QLineEdit()
                    self.inputs[i]=input
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1    
                case "date":
                    label_add=QLabel(i+' :')
                    input = QDateEdit(calendarPopup=True)
                    input.setDateTime(QDateTime.currentDateTime())
                    self.inputs[i]=input
                    Layout.addWidget(label_add,self.itemNumber,0,1,2)
                    Layout.addWidget(input,self.itemNumber,2,1,4)
                    self.itemNumber+=1  
                case "restricted_values":
                    label_add=QLabel(i+' :')
                    input = QComboBox()
                    input.addItems(self.getRestricted()[i])
                    self.inputs[i]=input
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
    
    '''add the row to the database and to the table'''
    
    def addRow(self):
        for i in list(self.inputs.keys()):
            match self.inputs[i].__class__.__name__:
                case "QLineEdit":
                    print("QLine")
                    self.setItem(self.count, att, QTableWidgetItem(str(getattr(i,headerH[att]))))
                case "QComboBox":
                    print("QComboBox")
                case "QDateEdit":
                    print("QDateEdit")