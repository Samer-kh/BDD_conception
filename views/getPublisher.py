from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from services.queries_service import *
from views.queryTable import *
class GetPublisher(QWidget):
    mainwidget=None
    buttons=[]
    def __init__(self,mainwidget,buttons):
        super().__init__()
        self.buttons=buttons
        self.mainwidget=mainwidget
        '''prepare the layout'''
        
        self.setWindowTitle("Query eight: publisher")
        Layout=QGridLayout()
        
        '''Prepare the widgets'''
        Label1=QLabel("Publisher :")
        self.input1=QLineEdit()
        Layout.addWidget(Label1,0,0,1,2) 
        Layout.addWidget(self.input1,0,2,1,6) 
        Button=QPushButton("Execute")
        Button.clicked.connect(self.query)
        Layout.addWidget(Button,1,0,1,6)
         
        '''set the layout'''
        
        self.setLayout(Layout)
        
        
        '''changing the style and the font of the window'''
    
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(11.5)
        QApplication.setFont(font, "QWidget")
        QApplication.setStyle("Fusion")
        
    def query(self):
        publisher=self.input1.text()
        (rows,keys) = execute_query_eight(publisher)
        newTable=QueryTable(rows,keys)
        self.mainwidget.Stacked_layout.itemAt(0).widget().setParent(None)
        self.mainwidget.widget=newTable
        self.mainwidget.Stacked_layout.addWidget(self.mainwidget.widget)
        self.buttons[0].setEnabled(False)
        self.buttons[1].setEnabled(False)
        self.buttons[2].setEnabled(False)  
        self.close()          
