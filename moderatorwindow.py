# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QKeyEvent
from PyQt4.QtCore import pyqtSignature, Qt,  SIGNAL

from ui.Ui_moderatorwindow import Ui_MainWindow
from mainwindow import MainWindow
import config

class ModeratorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Moderator Display')
        self.connect(self.Correct, SIGNAL("clicked()"), self.correctClicked)
        self.connect(self.Power, SIGNAL("clicked()"), self.powerClicked)
        self.connect(self.Negative, SIGNAL("clicked()"), self.wrongClicked)
        self.connect(self.Clear, SIGNAL("clicked()"), self.clearClicked)
        
    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if self.gameWindow.isBuzzer(event.text()):
                if not self.gameWindow.teamIsHighlighted():
                    for team in self.gameWindow.teamObjectList:
                        if event.text() in team.buzzerList:
                            buzzerIndex = team.buzzerList.index(event.text())
                            playerIndex = int(team.activePlayerList[buzzerIndex])
                            playerPicture = team.playerPictureList[playerIndex]
                            playerName = team.playerNameList[playerIndex]
                            teamWidget = team.teamWidget
                            self.gameWindow.buzzed(playerPicture, playerName, teamWidget)
            else:
                self.gameWindow.functionHandler(event.text())

    
    def powerClicked(self):
        self.gameWindow.changeScoreTossup(config.powerPoints)

    def correctClicked(self):
        self.gameWindow.changeScoreTossup(config.correctPoints)

    def wrongClicked(self):
        self.gameWindow.changeScoreTossupNeg(config.negPoints)

    def clearClicked(self):
        self.gameWindow.clearBuzzers()

    @pyqtSignature("")
    def on_actionNew_Game_triggered(self):
        from newgame import NewGameDialog
        self.newgame=NewGameDialog()
        from modules import databaseaccess
        teamsList = databaseaccess.get_Teams()
        self.newgame.team1.addItems(teamsList)
        self.newgame.team2.addItems(teamsList)
        self.newgame.show()
        self.connect(self.newgame.accept, SIGNAL("clicked()"), self.acceptedClicked)
        self.connect(self.newgame.reject, SIGNAL("clicked()"), self.rejectedClicked)


    def acceptedClicked(self):
        self.team1 = self.newgame.team1.currentText()
        self.team2 = self.newgame.team2.currentText()
        from modules import databaseaccess
        
        team1List = databaseaccess.get_Players_By_Team(self.team1)
        team2List = databaseaccess.get_Players_By_Team(self.team2)
        team1nameList = []
        team2nameList = []
        
        for player in team1List:
            team1nameList.append(databaseaccess.get_Player_Name_By_Id(player))
        
        for player in team2List:
            team2nameList.append(databaseaccess.get_Player_Name_By_Id(player))
        
        self.gameWindow = MainWindow()
        self.gameWindow.setupGame(self.team1,  self.team2)
        self.gameWindow.show()
        self.newgame.close()

    
    def rejectedClicked(self):
        self.newgame.close()
   
