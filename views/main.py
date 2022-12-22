import PySide2.QtCore
import sys
import re 
import functools


from PySide2.QtCore import (
    Qt,
    QEvent,
    QTimer,
    QUrl,
    QDir,
    QFileInfo
    )
from PySide2.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
    QSizePolicy,
    QTabWidget,
    QInputDialog,
    QComboBox,
    QStyledItemDelegate,
    QGridLayout,
    QDockWidget,
    QListWidget,
    QMessageBox,
    QStyle,
    QCheckBox,
    QSplashScreen,
    QFileDialog
)

from PySide2.QtGui import *


class GraphicalInterface(QMainWindow):
    tabs=0
    tabNumber=2
    ligne=0
    colonne=0
    nbrFigures=0
    discInit={}
    hideAttribute=False
    figures={}
    Buttons=[]
    
    screenshotName="DefaultName"
    saved=False
    Files={}
    FileNames=[]
    conf_file=[]
    conf_ok=False
    tabFig={}
    def __init__(self):
        super().__init__()
        self.figuresMat=[]
        self.setWindowTitle("Graphical Interface")
        self.Filechoisit=False
        #Layout configuration
        self.Stacked_layout=QStackedLayout()
        Page_layout=QVBoxLayout()
        Button_layout=QHBoxLayout()
        #Button_layout.setSpacing(100);
        #Button_layout.setContentsMargins(100,0,100,0)
        Page_layout.addLayout(Button_layout)
        Page_layout.addLayout(self.Stacked_layout)
        #button configuration
        button_add=QPushButton("Initialiser des Figures")
        
        button_onglet=QPushButton("Ajouter des onglets")
        button_choix_file=QPushButton("Choisir les fichiers")
        button_add_figure=QPushButton("Ajouter une figure ")
        button_save_figures=QPushButton("Sauvegarder les figures")
        button_configuration=QPushButton("")
        button_upload=QPushButton("")
        Box_desactivate_menu=QCheckBox()
        Logo=QLabel()
        #add the buttons to the list for save later
        self.Buttons.append(button_add)
        
        self.Buttons.append(button_onglet)
        self.Buttons.append(button_choix_file)
        self.Buttons.append(button_add_figure)
        self.Buttons.append(button_save_figures)
        self.Buttons.append(Box_desactivate_menu)
        self.Buttons.append(button_configuration)
        self.Buttons.append(button_upload)        
        self.Buttons.append(Logo)        
        #seeing icons
        pixmap=QPixmap("logo.png");
        Logo.setPixmap(pixmap)
        pixmapi_save = getattr(QStyle, "SP_DialogSaveButton")
        pixmapi_add = getattr(QStyle, "SP_MediaPlay")
        pixmapi_add_file=getattr(QStyle,"SP_ComputerIcon")
        pixmapi_addi = getattr(QStyle, "SP_DialogApplyButton")
        pixmapi_conf = getattr(QStyle , 'SP_FileLinkIcon')
        pixmapi_upload = getattr(QStyle , 'SP_FileDialogToParent')
        icon_save = self.style().standardIcon(pixmapi_save)
        icon_add = self.style().standardIcon(pixmapi_add)
        icon_pc=self.style().standardIcon(pixmapi_add_file)
        icon_addi = self.style().standardIcon(pixmapi_addi)
        icon_conf = self.style().standardIcon(pixmapi_conf)
        icon_upload = self.style().standardIcon(pixmapi_upload)
        
        button_add.setIcon(icon_add)
        button_add_figure.setIcon(icon_addi)
        button_choix_file.setIcon(icon_pc)
        button_onglet.setIcon(icon_addi)
        button_save_figures.setIcon(icon_save)
        button_configuration.setIcon(icon_conf)
        button_upload.setIcon(icon_upload)
        
        button_add.setFixedHeight(50)
        button_choix_file.setFixedHeight(50)
        
        button_onglet.setFixedHeight(50)
        button_add_figure.setFixedHeight(50)
        button_save_figures.setFixedHeight(50)
        Box_desactivate_menu.setFixedHeight(50)
        button_configuration.setFixedHeight(50)
        button_upload.setFixedHeight(50)
        button_configuration.setFixedWidth(50)
        button_upload.setFixedWidth(50)
        Logo.setFixedHeight(50)
        
        button_add.setSizePolicy(
        QSizePolicy.Preferred,
        QSizePolicy.Preferred)

  
        
        Button_layout.addWidget(button_add,Qt.AlignRight)
       
        Button_layout.addWidget(button_onglet,Qt.AlignRight)
        Button_layout.addWidget(button_choix_file,Qt.AlignRight)
        Button_layout.addWidget(button_add_figure,Qt.AlignRight)
        Button_layout.addWidget(button_save_figures,Qt.AlignRight)
        Button_layout.addWidget(button_configuration,Qt.AlignRight)
        Button_layout.addWidget(button_upload,Qt.AlignRight)
        Button_layout.addWidget(Box_desactivate_menu,Qt.AlignRight)

        Button_layout.addWidget(Logo,Qt.AlignLeft)
        #tab system
        self.tabNumber=2
        self.tabs=QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.delete)
        self.tabs.currentChanged.connect(self.TabChanged)
        self.countTabs=0
        tab=QWidget()
        tab.setLayout(QGridLayout())
        self.tabs.addTab(tab,"Onglet1")
        #self.discInit[0]=False
        self.Stacked_layout.addWidget(self.tabs)
        
        #Actions des Boutons
        
        button_onglet.clicked.connect(self.add_tab)
        button_add.clicked.connect(self.add_figure)
        button_add_figure.clicked.connect(self.add_figure_at_specified_location)
        Box_desactivate_menu.stateChanged.connect(self.hide)
        button_save_figures.clicked.connect(self.save_images)
        button_choix_file.clicked.connect(self.readFile)
        button_configuration.clicked.connect(self.Config_file)
        button_upload.clicked.connect(self.Conf_upload)
        #configuration du font
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        QApplication.setFont(font, "QWidget")
        
        QApplication.setStyle("Fusion")
        
        widget=QWidget()
        widget.setLayout(Page_layout)
        self.setCentralWidget(widget)

            
    def TabChanged(self):
        if (self.countTabs>0):
            theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
            if (self.conf_ok==True):
                self.conf_file.write("tab_changed "+ str(self.tabs.currentIndex()))
                self.conf_file.write(' \n')            
        else:
            self.countTabs+=1
    def sameFilesOrNot(self,lines):
        ok=[]
        for i in list(eval(lines[1]).keys()):
            set=False
            for j in list(self.Files.keys()):
                if ((i[0:11]==j[0:11])or(i[0:9]==j[0:9])):
                    ok.append(True)
                    set=True
            if (set==False):
                ok.append(False)
        for i in ok:
            if i==False:
                return False
        return True
    
    def sameFiles(self,discFile):
        for i in list(discFile.keys()):
            if i not in list(self.Files.keys()):
                return False
        return True
    def regelateList(self,listAtt):
        results=[]
        resultsFinal=[]
        listBan=[]
        order=[]
        ko=False
        for i in listAtt:
            fileAchanger=i.split(":")[0]
            for j , k in self.Files.items():
                if ((j[0:14]==fileAchanger[0:14]=="results_master")or(j[0:13]==fileAchanger[0:13]=="results_slave")or(j[0:10]==fileAchanger[0:10]=="data_elise")and(j not in listBan)):
                    for i in listAtt:
                        if (i.split(":")[0]==fileAchanger):
                            results.append(j+":"+i.split(":")[1])
                            order.append(listAtt.index(i))
                    listBan.append(j)
        for k in order:
            resultsFinal.append(results[k])
        return resultsFinal
    def equivalentFile(self,file):
        for i in list(self.Files.keys()):
            if ((i[0:14]==file[0:14]=="results_master")or(i[0:13]==file[0:13]=="results_slave")or(i[0:10]==file[0:10]=="data_elise")):
                 return i
    def Conf_upload(self):
        if (len(self.Files)>0):
            Opener = QFileDialog()
            filenames = Opener.getOpenFileNames(self, "Choisir un fichier de configuration")
            print(filenames)
            if (len(filenames[0])==1):
                file=open(filenames[0][0],"r")
                lines=file.readlines()
                if (int(lines[0])==len(self.Files)):
                    if (self.sameFilesOrNot(lines)):
                        print(lines)
                        for i in range(2,len(lines),1):
                            args=lines[i].split(" ")
                            if (args[0]=="initialiser_figure"):
                                self.initFigConf(args[1],args[2])
                                
                            elif (args[0]=="inject_figure"):
                                self.injectFigConf(args[1],args[2])
                            elif (args[0]=="add_tab"):
                                self.add_tab()
                            elif (args[0]=="delete_tab"):
                                self.delete(int(args[1]))
                            elif (lines[i][0:16]=="execute_addition"):
                                args=lines[i].split("#")
                                figurees=self.tabFig[float(args[8])]
                                coord=eval(args[7])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        c=fgw.FigureControlWindow(k[0].sc,k[0],k[0].discSelect,k[0].champsChoisis,k[0].conf_file,k[0].conf_ok,k[0].ligne,k[0].colonne,k[0].t)
                                        c.checkChosen()
                                        if ((len(self.Files)>1)and(self.sameFiles(k[0].discFile))):
                                            c.toWhatAdd.setCurrentText(self.equivalentFile(args[3].split(":")[0])+":"+args[3].split(":")[1])
                                        else:
                                            c.toWhatAdd.setCurrentText(args[3])
                                        c.SommeChoix.setCurrentText(args[2])
                                        if (len(self.Files)==1):
                                            c.functionCombo.setCurrentText(args[5])
                                        elif (len(self.Files)>1):
                                            if (self.sameFiles(k[0].discFile)):
                                                c.functionCombo.setCurrentText(args[5])
                                            else:
                                                c.functionCombo.setCurrentText(self.equivalentFile(args[5]))
                                        c.CourbeChoix.setCurrentText(args[1])
                                        c.manipulateCourbe()
                                        #k[0].sommeDiff(args[1],args[2],args[3],eval(args[4]),args[5],args[6])
                            elif (lines[i][0:12]=="execute_mult"):
                                args=lines[i].split("#")
                                figurees=self.tabFig[float(args[4])]
                                coord=eval(args[3])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        fig=k[0]
                                        c=fgw.FigureControlWindow(fig.sc,fig,fig.discSelect,fig.champsChoisis,fig.conf_file,fig.conf_ok,fig.ligne,fig.colonne,fig.t)
                                        c.checkChosen()
                                        if (len(self.Files)==1):
                                            fig.coeffApp(float(args[1]),eval(args[2]),eval(args[5]),c.ChampComboBox)
                                        elif(len(self.Files)>1):
                                            if (self.sameFiles(eval(lines[1]))):
                                                fig.coeffApp(float(args[1]),eval(args[2]),eval(args[5]),c.ChampComboBox)   
                                            else:
                                                results=self.regelateList(eval(args[2]))
                                                allItems=self.regelateList(eval(args[5]))
                                                allItems=list(set(allItems))
                                                fig.coeffApp(float(args[1]),results,allItems,c.ChampComboBox)
                            elif (lines[i][0:11]=="execute_off"):
                                args=lines[i].split("#")
                                figurees=self.tabFig[float(args[4])]
                                coord=eval(args[3])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        fig=k[0]
                                        c=fgw.FigureControlWindow(fig.sc,fig,fig.discSelect,fig.champsChoisis,fig.conf_file,fig.conf_ok,fig.ligne,fig.colonne,fig.t)
                                        c.checkChosen()
                                        if (len(self.Files)==1):
                                            fig.OffApp(float(args[1]),eval(args[2]),eval(args[5]),c.ChampComboBox)
                                        elif(len(self.Files)>1):
                                            if (self.sameFiles(eval(lines[1]))):
                                                fig.OffApp(float(args[1]),eval(args[2]),eval(args[5]),c.ChampComboBox)   
                                            else:
                                                results=self.regelateList(eval(args[2]))
                                                allItems=self.regelateList(eval(args[5]))
                                                allItems=list(set(allItems))
                                                fig.OffApp(float(args[1]),results,allItems,c.ChampComboBox)
                            elif (args[0]=="change_axe_time"):
                                figurees=self.tabFig[float(args[2])]
                                coord=eval(args[1])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        fig=k[0]
                                        fig.axisTime()
                                        fig.sc.ax.set_xlabel("Temps(s)")
                                        
                                        fig.t=True
                            elif (args[0]=="change_axe_sample"):
                                figurees=self.tabFig[float(args[3])]
                                coord=eval(args[2])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        fig=k[0]
                                        fig.axisSample()
                                        fig.sc.ax.set_xlabel("Echantillons")
                                        
                            elif (args[0]=="execute_off"):
                                print("")
                            elif (lines[i][0:5]=="check"):
                                args=lines[i].split("#")
                                print(args)
                                index=self.get_indices("Onglet"+str(args[3]).split(".")[0])[0]
                                self.tabs.setCurrentIndex(index)
                                print(self.figures)
                                figurees=self.tabFig[float(args[3])]
                                coord=eval(args[2])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        fig=k[0]
                                        fig.discSelect=self.reglateDiscSelect(eval(args[1]))
                                        fig.recheckItems()
                                        
                            elif (lines[i][0:9]=="col_check"):
                                args=lines[i].split("#")
                                champs=eval(args[1])
                                index=self.get_indices("Onglet"+str(args[3]).split(".")[0])[0]
                                self.tabs.setCurrentIndex(index)
                                figurees=self.tabFig[float(args[3])]
                                coord=eval(args[2])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        k[0].champsChoisis=champs
                            elif (args[0]=="tab_changed"):
                                self.tabs.setCurrentIndex(int(args[1]))
                            elif (lines[i][0:10]=="Affich_col"):
                                args=lines[i].split("#")
                                index=self.get_indices("Onglet"+str(args[2]).split(".")[0])[0]
                                self.tabs.setCurrentIndex(index)
                                figurees=self.tabFig[float(args[2])]
                                coord=eval(args[1])
                                for k in figurees:
                                    if ((k[1]==coord[0])and(k[2]==coord[1])):
                                        c=fgw.FigureControlWindow(k[0].sc,k[0],k[0].discSelect,k[0].champsChoisis,k[0].conf_file,k[0].conf_ok,k[0].ligne,k[0].colonne,k[0].t)
                                        c.checkChosen()
                                        c.redrawColumns()
                            
                    else:
                        self.Error_msg("type de fichier est incompatible")
                else:
                    self.Error_msg("Nombre de fichier incompatible")
            elif(len(filenames[0])>1):
                self.Error_msg("Merci de choisir un seul fichier de configuration")
            else:
                self.Error_msg("Merci de choisir un fichier de configuration")
        else:
            self.Error_msg("Merci de choisir les fichiers d'abord")
    def reglateDiscSelect(self,disc):
        results={}
        listban=[]
        for j in list(self.Files.keys()):
            for i in list(disc.keys()):
                if (((i[0:14]==j[0:14]=="results_master")and(j not in listban))or(i==j)):
                    results[j]=disc[i]
                    listban.append(j)
                if (((i[0:13]==j[0:13]=="results_slave")and(j not in listban))or(i==j)):
                    results[j]=disc[i]
                    listban.append(j)
                if (((i[0:10]==j[0:10]=="data_elise")and(j not in listban))or(i==j)):
                    results[j]=disc[i]
                    listban.append(j)
        return results
    def injectFigConf(self,coord,tabIndex):
        coordTup=eval(coord)
        ligne,colonne=coordTup[0],coordTup[1]
        selectedTab=self.tabs.currentWidget()
        Grid=selectedTab.layout()
        attachable=QClosingDockWidget(ligne,colonne,self.controlLayout,self.verif_reinitialisation,self.figures,self.tabs)
        figura=fm.figure([],[],ligne-1,colonne-1,"default",self.Files,self.FileNames,self.conf_file,self.conf_ok,selectedTab)
        self.figuresMat.append((figura,(ligne,colonne)))
        attachable.setWidget(figura)
        attachable.setFeatures(QDockWidget.DockWidgetClosable)
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if(len(theIndex)==0):
            theIndex.append(0)
        self.figures[theIndex[0]].append((attachable,ligne-1,colonne-1))
        self.tabFig[theIndex[0]].append((figura,ligne-1,colonne-1))
        Grid.addWidget(attachable,ligne-1,colonne-1)
        selectedTab.setLayout(Grid)        
    def initFigConf(self,coord,tabIndex):
        print(coord)
        coordTup=eval(coord)
        ligne,colonne=coordTup[0],coordTup[1]
        selectedTab=self.tabs.currentWidget()
        Grid=selectedTab.layout()
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if (len(theIndex)==0):
            theIndex.append(0)
        ListAtt=[]
        ListFig=[]
        for i in range(0,ligne,1):
            for j in range(0,colonne,1):
                Attachable=QClosingDockWidget(i,j,self.controlLayout,self.verif_reinitialisation,self.figures,self.tabs)
                figura=fm.figure([],[],i,j,"default",self.Files,self.FileNames,self.conf_file,self.conf_ok,selectedTab)
                self.figuresMat.append((figura,(i+1,j+1)))
                Attachable.setWidget(figura)
                Attachable.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetMovable)
                ListAtt.append((Attachable,i,j))
                ListFig.append((figura,i,j))
                Grid.addWidget(Attachable,i,j)
        self.figures[theIndex[0]]=ListAtt
        self.tabFig[theIndex[0]]=ListFig
        selectedTab.setLayout(Grid)
        self.discInit[theIndex[0]]=True       
    def Config_file(self,text):
        if ((self.conf_ok==False)and(len(self.Files)>0)):
            
            pop_up=QInputDialog()
            text, ok = pop_up.getText(self, 'Nom du fichier', 'Spécifier le nom du fichier de configuration:')
            if (ok):
                self.conf_file=open(text+".txt",'w')
                self.conf_ok=True
                self.conf_file.write(str(len(self.Files)))
                self.conf_file.write(' \n')
                self.conf_file.write(str(self.Files))            
                self.conf_file.write(' \n')

                    
                self.Success_msg("L'enregistrement de la configuration a commencé")
        elif (self.conf_ok==True):
            self.conf_ok=False
            self.Success_msg("Le fichier de configuration est bien enregistrer")
            self.conf_file.close()

        else:
            self.Error_msg("Merci de choisir les fichiers d'abord")
                
    def readFile(self):
        Opener = QFileDialog()
        backup={}
        if (len(self.Files)>0):
            backup=self.Files
        while(True):
            
            filenames = Opener.getOpenFileNames(self, "Choisir un fichier")
            
            if(len(filenames[0])>0):
                self.Success_msg("Fichier bien lu ")
                self.Filechoisit=True
#                 self.Files={}
                break
            elif (len(filenames[0])==0):
                self.Error_msg("Choisir un fichier svp !")
#                 self.Files={}
                
                if (len(backup)>0):
                    self.Files=backup
                    break
            else:
                self.Error_msg("Fichier choisit est incorrect")
        
        self.FileNames=filenames
        print(self.FileNames)
        for i in range(0,len(filenames[0]),1):
            url = QUrl.fromLocalFile(filenames[0][i])
            d=QDir()
            absolute=""
            d=QFileInfo(filenames[0][i]).absoluteDir()
            absolute=d.absolutePath();
            if (url.fileName()[len(url.fileName())-4]=="."):
                if (url.fileName()[len(url.fileName())-3:len(url.fileName())])=="dat":
                    self.Files[url.fileName()[0:len(url.fileName())]]=absolute[0:len(absolute)]
                else:
                    self.Files[url.fileName()[0:len(url.fileName())-4]]=absolute[0:len(absolute)]
            else:
                self.Files[url.fileName()[0:len(url.fileName())]]=absolute[0:len(absolute)]
      
    
            

    def setFont(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        QApplication.setFont(font, "QWidget")
    def Success_msg(self,txt):
        self.setFont()
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
        self.setFont()
        msg = QMessageBox(self)
        msg.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Erreur :")
        msg.setInformativeText(txt)
        msg.setWindowTitle("Message d'erreur")
        msg.setStandardButtons(QMessageBox.Ok)
        
        
        msg.exec_()
    def take_screen_shot(self):
            index=self.tabs.currentIndex()
            screen = QApplication.primaryScreen()
            self.tabs.setCurrentIndex(index)
            screenshot =  screen.grabWindow( widget.winId())
            ok=screenshot.save(self.screenshotName+'.jpg', 'jpg')
            self.saved=True
        
    def save_images(self):
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        QApplication.setFont(font, "QWidget")
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if (len(theIndex)==0):
            theIndex.append(0)
        if(theIndex[0] in self.discInit.keys()):
            indexSelected=self.tabs.currentIndex()
            if(self.hideAttribute==False):
                self.hide()
                for i in self.Buttons:
                    i.setVisible(False)
                for i in range(0,self.tabs.count(),1):
                    if(i!=indexSelected):
                        self.tabs.setTabEnabled(i,False) 
                        # set the style sheet
                        default_style_sheet = self.tabs.styleSheet()
                        self.tabs.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
                self.tabs.setTabEnabled(indexSelected,False)
                default_style_sheet = self.tabs.styleSheet()
                self.tabs.setStyleSheet("QTabBar::tab::disabled {width: 0; height: 0; margin: 0; padding: 0; border: none;} ")
            pop_up=QInputDialog()
            text, ok = pop_up.getText(self, 'Sauvegarder les figures', 'Spécifier le nom de l\'image:')
            if ok :
                self.screenshotName=text
                self.take_screen_shot()
            for i in self.Buttons:
                i.setVisible(True)
            for i in range(0,self.tabs.count(),1):
                self.tabs.setTabEnabled(i,True) 
                    # set the style sheet
                self.tabs.setStyleSheet(default_style_sheet)
            font = QFont()
            font.setFamily("Arial")
            font.setPointSize(13)
            QApplication.setFont(font, "QWidget")
            if(self.hideAttribute==True):
                self.hide()
            if(self.saved==True):
                self.Success_msg("Figures sauvegardées")
                self.saved=False
        else:
            self.Error_msg("Initialiser les figures avant de les sauvegarder ! ")

    def hide(self):
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if (len(theIndex)==0):
            theIndex.append(0)
        
        if(len(self.figures[theIndex[0]])>0):
            theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
            if(len(theIndex)==0):
                theIndex.append(0)
            listFiguresOfTab=self.figures[theIndex[0]]
            if(self.hideAttribute==False):
                for i in listFiguresOfTab:
                    figure=i[0].widget()
                    items=figure.getHidableWidgets()
                    for j in items:
                        j.setVisible(False)
                    i[0].setFeatures(QDockWidget.NoDockWidgetFeatures)
                    self.hideAttribute=True
            else:
                for i in listFiguresOfTab:
                    figure=i[0].widget()
                    items=figure.getHidableWidgets()
                    for j in items:
                        j.setVisible(True)
                    i[0].setFeatures(QDockWidget.DockWidgetClosable)
                    self.hideAttribute=False
        else:
            for i in self.Buttons:
                if type(i)==type(QCheckBox()):
                    i.setChecked(False)
                    self.Error_msg("Initialiser les figures d'abord ")
    def verifFigures(self,ligne,colonne):
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if(len(theIndex)==0):
            theIndex.append(0)
        for i in self.figures[theIndex[0]]:

            if (i[1]==ligne-1)and(i[2]==colonne-1):
                return True
        return False
          
        
    def add_figure_at_specified_location(self):
        print(self.discInit)
        selectedTab=self.tabs.currentWidget()
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if (len(theIndex)==0):
            theIndex.append(0)
        if(theIndex[0] not in self.discInit.keys()):
            self.Error_msg("Initialiser les figures d'abord")
        else:
            pop_up=QInputDialog()
            text, ok = pop_up.getText(self, 'Ajouter une figure', 'Spécifier la taille du grid : l,c ?')
            if (ok):
                txt=tuple(text)
                try:
                    ligne,colonne=int(txt[0]),int(txt[2])
                except (RuntimeError, ValueError, NameError):
                    self.Error_msg("il faut suivre la forme : l,c")
                    return False
                if(self.verifFigures(ligne,colonne)):
                    self.Error_msg("déja existant!! ")
                    return False
                Grid=selectedTab.layout()
                attachable=QClosingDockWidget(ligne,colonne,self.controlLayout,self.verif_reinitialisation,self.figures,self.tabs)
                data = np.random.randn(100, 2)
                figura=fm.figure([],[],ligne-1,colonne-1,"default",self.Files,self.FileNames,self.conf_file,self.conf_ok,theIndex[0],selectedTab)
                self.figuresMat.append((figura,(ligne,colonne)))
                attachable.setWidget(figura)
                attachable.setFeatures(QDockWidget.DockWidgetClosable)
                theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
                if(len(theIndex)==0):
                    theIndex.append(0)
                self.figures[theIndex[0]].append((attachable,ligne-1,colonne-1))
                self.tabFig[theIndex[0]].append((figura,ligne-1,colonne-1))
                Grid.addWidget(attachable,ligne-1,colonne-1)
                selectedTab.setLayout(Grid)
                if (self.conf_ok==True):
                    self.conf_file.write("inject_figure " +str((ligne,colonne)).replace(" ", "") +" "+str(theIndex[0]))
                    self.conf_file.write(' \n')
    def get_indices(self,tab_name):
        return [index for index in range(self.tabs.count())
            if tab_name == self.tabs.tabText(index)]           
    def add_tab(self):
        tab=QWidget()
        tab.setLayout(QGridLayout())
        self.tabs.addTab(tab,"Onglet"+str(self.tabNumber) )
       # self.discInit[self.tabNumber]=False
        self.tabNumber+=1
        if (self.conf_ok==True):
            self.conf_file.write("add_tab")
            self.conf_file.write(' \n')

    def delete(self, index):
        if (self.tabs.count()>1):
            theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(index))]
            if(len(theIndex)==0):
                theIndex.append(0)
            self.tabs.removeTab(index)
            if (theIndex[0] in self.discInit.keys()):
                del self.discInit[theIndex[0]]
                
                del self.figures[theIndex[0]]
            if (self.conf_ok==True):
                self.conf_file.write("delete_tab "+str(index))
                self.conf_file.write(' \n')            

    def verif_reinitialisation(self):
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if (len(theIndex)==0):
            theIndex.append(0)
        if ((theIndex[0]  in self.discInit.keys())):
            del self.discInit[theIndex[0]]
    def add_figure(self):
        if(self.Filechoisit):
            theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
            if (len(theIndex)==0):
                theIndex.append(0)
            if(theIndex[0] not in self.discInit.keys()):
                selectedTab=self.tabs.currentWidget()
                (ligne,colonne),(n,m),txt=(0,0),(0,0),""
                pop_up=QInputDialog()
                self.setFont()
                text, ok = pop_up.getText(self, 'Intialisation des figures', 'Nombre de figures à afficher (lignes,colonnes):l,c ?')
                if ok:
                    txt=tuple(text)
                    try:
                        self.ligne,self.colonne=int(txt[0]),int(txt[2])
                    except (RuntimeError, ValueError, NameError):
                        self.Error_msg("il faut suivre la forme : l,c")
                        return False;
                    ligne,colonne=int(txt[0]),int(txt[2])
                    self.nbrFigures=self.ligne*self.colonne
                    Grid=selectedTab.layout()
                    theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
                    if (len(theIndex)==0):
                        theIndex.append(0)
                    ListAtt=[]
                    ListFig=[]
                    for i in range(0,ligne,1):
                        for j in range(0,colonne,1):
                                Attachable=QClosingDockWidget(i,j,self.controlLayout,self.verif_reinitialisation,self.figures,self.tabs)
                                data = np.random.randn(100, 2)
                                figura=fm.figure([],[],i,j,"default",self.Files,self.FileNames,self.conf_file,self.conf_ok,theIndex[0],selectedTab)
                                self.figuresMat.append((figura,(i+1,j+1)))
                                Attachable.setWidget(figura)
                                Attachable.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetMovable)
                                ListAtt.append((Attachable,i,j))
                                ListFig.append((figura,i,j))
                                Grid.addWidget(Attachable,i,j)
                    self.figures[theIndex[0]]=ListAtt
                    self.tabFig[theIndex[0]]=ListFig
                    print(self.figures)
                    selectedTab.setLayout(Grid)
                    #selectedTab.update()
                    self.discInit[theIndex[0]]=True
                    if (self.conf_ok==True):
                        print(colonne)
                        self.conf_file.write("initialiser_figure " +str((ligne,colonne)).replace(" ", "") +" "+str(theIndex[0]))
                        self.conf_file.write(' \n')
            else:
                self.Error_msg("Les figures sont déjà initialisées")
        else:
            self.Error_msg("Choisir un fichier d'abord !!! ")
#permet de réarranger les figures selon l'ordre normal 
            
       
#controller le layout
    def controlLayout(self):
        grid=self.tabs.currentWidget().layout()
        index = grid.count()

        if (index==0):
            theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
            if(len(theIndex)==0):
                theIndex.append(0)
            del self.discInit[theIndex[0]]
  
  

class QClosingDockWidget(QDockWidget):
    ligne=0
    colonne=0
    control=0
    verif=0
    figures={}
    tabs=0
    def __init__(self,ligne,colonne,control,verif,figures,tabs,parent=None):
        QDockWidget.__init__(self,parent)
        self.control=control
        self.verif=verif
        self.figures=figures
        self.tabs=tabs
    def closeEvent(self,event):
        self.setParent(None)
        event.accept()
        self.control()
        theIndex=[float(s) for s in re.findall(r'-?\d+\.?\d*', self.tabs.tabText(self.tabs.currentIndex()))]
        if(len(theIndex)==0):
            theIndex.append(0)
        grid=self.tabs.currentWidget().layout()
        index = grid.count()
        if (theIndex[0] in self.figures.keys()):
            for i in self.figures[theIndex[0]]:
                if(i[0]==self):
                    self.figures[theIndex[0]].remove(i)
            if(len(self.figures[theIndex[0]])==0):
                del self.figures[theIndex[0]]
        self.verif()
  
        
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    
    widget=GraphicalInterface()
    widget.resize(1000,1000)
    widget.show()
    app.exec_()
    sys.exit()