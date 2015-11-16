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
        self.connect(self.Timer,  SIGNAL("clicked()"), self.timerClicked)
        self.connect(self.Previous, SIGNAL("clicked()"), self.previousClicked)
        self.connect(self.Next,  SIGNAL("clicked()"),  self.nextClicked)
        
        
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
        self.gameWindow.functionHandler(config.powerButton)

    def correctClicked(self):
        self.gameWindow.functionHandler(config.correctButton)

    def wrongClicked(self):
        self.gameWindow.functionHandler(config.negButton)

    def clearClicked(self):
        self.gameWindow.functionHandler(config.clearButton)
    
    def timerClicked(self):
        self.gameWindow.functionHandler(config.startTimer)

    def previousClicked(self):
        self.gameWindow.functionHandler(config.previousQuestion)
    
    def nextClicked(self):
        self.gameWindow.functionHandler(config.nextQuestion)

    @pyqtSignature("")
    def on_actionNew_Game_triggered(self):
        from newgame import NewGameDialog
        self.newgame=NewGameDialog()
        from modules import databaseaccess
        teamsDict = databaseaccess.get_Teams()
        for team_id in teamsDict:
            self.newgame.team1.addItem(teamsDict[team_id], team_id)
            self.newgame.team2.addItem(teamsDict[team_id], team_id)
        self.newgame.show()
        self.connect(self.newgame.accept, SIGNAL("clicked()"), self.acceptedClicked)
        self.connect(self.newgame.reject, SIGNAL("clicked()"), self.rejectedClicked)


    def acceptedClicked(self):
        self.gameWindow = MainWindow()
        self.gameWindow.team1 = self.newgame.team1.currentText()
        self.gameWindow.team2 = self.newgame.team2.currentText()
        team1index = self.newgame.team1.currentIndex()
        team2index = self.newgame.team2.currentIndex()
        self.gameWindow.team1id = self.newgame.team1.itemData(team1index).toString()
        self.gameWindow.team2id = self.newgame.team2.itemData(team2index).toString()
        from modules import databaseaccess
        team1List = databaseaccess.get_Player_Name_By_Team_Id(self.gameWindow.team1id)
        team2List = databaseaccess.get_Player_Name_By_Team_Id(self.gameWindow.team2id)
        team1nameList = []
        team2nameList = []
        self.connect(self.gameWindow, SIGNAL('previousQuestion'),  self.previousQuestion)
        self.connect(self.gameWindow, SIGNAL('nextQuestion'),  self.nextQuestion)
        self.gameWindow.setupGame(self.gameWindow.team1, self.gameWindow.team2)
        self.gameWindow.show()
        self.newgame.close()
    
    def rejectedClicked(self):
        self.newgame.close()
   
    def previousQuestion(self):
        from modules import databaseaccess
        self.gameWindow.questionNumber = self.gameWindow.questionNumber - 1
        questionList = databaseaccess.get_Question_By_Id(self.gameWindow.questionNumber)
        self.Question.setText(questionList[0])
        self.Answer.setText(questionList[1])

    def nextQuestion(self):
        from modules import databaseaccess
        self.gameWindow.questionNumber = self.gameWindow.questionNumber + 1
        questionList = databaseaccess.get_Question_By_Id(self.gameWindow.questionNumber)
        self.Question.setText(questionList[0])
        self.Answer.setText(questionList[1])
