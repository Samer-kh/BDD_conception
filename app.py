from flask import Flask           # import flask

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import sys
from views.mainWidow import *
app = Flask(__name__)             # create an app instance

if __name__ == "__main__":        # on running python app.py
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
    widget.resize(1000,700)
    widget.show()
    app.exec_()
    sys.exit()