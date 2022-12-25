from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from persistance.author import *
from persistance.publication import *
from services.publication_service import *
from services.author_service import *
class DeleteWindow(QWidget):
    table="Publication"
    input=None
    def __init__(self,table,att,tableWidget):
        super().__init__()
        self.table=table
        self.Attributes=att
        self.tableWidget=tableWidget

        
        '''prepare the layout'''
        
        self.setWindowTitle("delete row")
        Layout=QGridLayout()
        
        ''' adding the deleting widgets based of the attribute type
                if the attribute is :
                    id => writing line 
        '''
        id=list(self.Attributes.keys())[0]
        label_add=QLabel(id+' :')
        self.input=QLineEdit()
        Layout.addWidget(label_add,0,0,1,2)
        Layout.addWidget(self.input,0,2,1,4)

                    
        button_validation=QPushButton("Delete row")    
        button_validation.clicked.connect(self.deleteRow)    
        Layout.addWidget(button_validation,1,0,1,6)  
                                          
        ''' add the layout to the widget '''   
        
        self.setLayout(Layout)
        
        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        
    def deleteRow(self):
        value=self.input.text()
        try:
            match self.table:
                case "Publication":
                    delete_publication(value)
                    self.Success_msg("Ligne supprimé avec succés")
                case "Authers":
                    delete_authors(value)
                    self.Success_msg("Ligne supprimé avec succés")
            self.tableWidget.refreshTable()
        except:
            self.Error_msg("Merci de vérifier les contraites avant de supprimer")
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