# -*- coding: utf-8 -*-

from PyQt4.QtGui import QMainWindow, QKeyEvent
from PyQt4.QtCore import pyqtSignature, Qt

from ui.Ui_mainwindow import Ui_MainWindow
from ui.teamwidget import TeamWidget
from ui.playerwidget import PlayerWidget
from modules.teamobject import TeamObject
import config

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle('Quizbowl Scorekeeper')
        self.tournamentLabel.setText(config.tournamentName)
        self.roundLabel.setText('Round: ' + config.roundNumber)
        self.playerWidget = PlayerWidget()
        self.playerWidgetLayout.addWidget(self.playerWidget)
        self.blankPlayerWidget()
        self.constructTeams(team1,  team2)
        
        

    def keyPressEvent(self, event):
        if type(event) == QKeyEvent:
            if self.isBuzzer(event.text()):
                if not self.teamIsHighlighted():
                    for team in self.teamObjectList:
                        if event.text() in team.buzzerList:
                            buzzerIndex = team.buzzerList.index(event.text())
                            playerIndex = int(team.activePlayerList[buzzerIndex])
                            playerPicture = team.playerPictureList[playerIndex]
                            playerName = team.playerNameList[playerIndex]
                            teamWidget = team.teamWidget
                            self.buzzed(playerPicture, playerName, teamWidget)
            else:
                self.functionHandler(event.text())

    def bonusModeChooser(self, points):
        if config.bonusMode:
            self.changeScore(points)
        else:
            self.changeScoreFinal(points)

    def buzzed(self, playerPicture, playerName, teamWidget):
        self.changePlayerWidget(playerPicture, playerName)
        self.highlightTeam(teamWidget)

    def blankPlayerWidget(self):
        self.playerWidget.updateWidget(config.blankPlayerPicture, '')

    def changePlayerWidget(self, picture, name):
        self.playerWidget.updateWidget(picture, name)

    def changeScoreBonus(self, scoreChange):
        for team in self.teamObjectList:
            if team.teamWidget.isHighlighted() and team.teamWidget.isBonus():
                team.teamWidget.setScore(team.teamWidget.getScore() + scoreChange)
                self.deHighlightTeam(team.teamWidget)
                team.teamWidget.bonusOff()
                self.blankPlayerWidget()

    def changeScoreTossup(self, scoreChange):
        for team in self.teamObjectList:
            if team.teamWidget.isHighlighted() and not team.teamWidget.isBonus():
                team.teamWidget.setScore(team.teamWidget.getScore() + scoreChange)
                if config.bonusMode:
                    team.teamWidget.bonusOn()
                else:
                    self.clearBuzzers()

    def changeScoreTossupNeg(self, scoreChange):
        for team in self.teamObjectList:
            if team.teamWidget.isHighlighted() and not team.teamWidget.isBonus():
                team.teamWidget.setScore(team.teamWidget.getScore() + scoreChange)
                self.clearBuzzers()

    def clearBuzzers(self):
        for team in self.teamObjectList:
            if team.teamWidget.isHighlighted():
                self.deHighlightTeam(team.teamWidget)
                team.teamWidget.bonusOff()
        self.blankPlayerWidget()
        
    def constructTeams(self,  team1,  team2):
        
        self.teamObjectList = []
        for team in config.teamList:
            teamFile = open(team, 'r')
            teamName = teamFile.readline().rstrip()
            playerPictureList = []
            playerNameList = []
            for line in teamFile:
                lineList = line.rstrip().split()
                playerNameList.append(lineList[0])
                playerPictureList.append(team.rsplit('/', 1)[0] + '/' + lineList[1])
            teamFile.close()
        """
        from modules import databaseaccess
        
            ##buzzerList = config.buzzerList[config.teamList.index(team)]
        activePlayerList = config.activePlayerList[config.teamList.index(team)]
        teamWidget = TeamWidget(team1)
        self.teamsLayout.addWidget(teamWidget)
        teamWidget = TeamWidget(team2)
        self.teamsLayout.addWidget(teamWidget)
        """
        print team1,  playerPictureList,  playerNameList,  buzzerList,  activePlayerList,  teamWidget
        teamObject = TeamObject(team1, playerPictureList, playerNameList, buzzerList, activePlayerList, teamWidget)
        self.teamObjectList.append(teamObject)

    def deHighlightTeam(self, teamWidget):
        teamWidget.deHighlight()

    def functionHandler(self, keyPress):
        if keyPress == config.clearButton:
            self.clearBuzzers()
        elif keyPress == config.negButton:
            self.changeScoreTossupNeg(config.negPoints)
        elif keyPress == config.correctButton:
            self.changeScoreTossup(config.correctPoints)
        elif keyPress == config.powerButton:
            self.changeScoreTossup(config.powerPoints)
        if keyPress == config.oneBonus:
            self.changeScoreBonus(config.bonusPoints)
        elif keyPress == config.twoBonus:
            self.changeScoreBonus(2 * config.bonusPoints)
        elif keyPress == config.threeBonus:
            self.changeScoreBonus(3 * config.bonusPoints)

    def highlightTeam(self, teamWidget):
        teamWidget.highlight()

    def isBuzzer(self, text):
        status = False
        for team in self.teamObjectList:
            if text in team.buzzerList:
                status = True
        return status

    def teamIsHighlighted(self):
        status = False
        for team in self.teamObjectList:
            if team.teamWidget.isHighlighted():
                status = True
        return status
