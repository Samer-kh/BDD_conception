from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
from services.publication_service import *
from services.author_service import *
from views.UpdateWindow import *
from services.user_service import *
from services.lab_service import *
from services.keyword_service import *
from services.echange_service import *
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
        try:
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
                case "Cost":
                    cost=get_cost(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,cost)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()
                case "Exchange":
                    ex=get_echange(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,ex)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()
                case "Category":
                    cat=get_categories(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,cat)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()
                case "User":
                    user=get_users(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,user)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()
                case "Lab":
                    lab=get_lab(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,lab)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()                    
                case "Keyword":
                    keyword=get_keyword(value)
                    updateWindow=UpdateWindow(self.table,self.Attributes,self.tableWidget,keyword)
                    self.updateWindow=updateWindow      
                    updateWindow.show()
                    self.close()                    
        except Exception:
            self.Error_msg("id n'existe pas. Vérifiez bien l'id avant de procéder")
        self.tableWidget.refreshTable()
        
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