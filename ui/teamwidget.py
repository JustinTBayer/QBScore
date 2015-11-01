from PyQt4.QtGui import QWidget

from Ui_teamwidget import Ui_TeamWidget

class TeamWidget(QWidget, Ui_TeamWidget):
    def __init__(self, name, score = 0):
        QWidget.__init__(self)
        self.ui = Ui_TeamWidget()
        self.ui.setupUi(self)
        self.setName(name)
        self.setScore(score)
        self.originalStyleSheet = self.ui.teamName.styleSheet()
        self.bonus = False
        self.highlighted = False

    def bonusOff(self):
        self.bonus = False

    def bonusOn(self):
        self.bonus = True

    def deHighlight(self):
        self.ui.teamName.setStyleSheet(self.originalStyleSheet)
        self.ui.teamScore.setStyleSheet(self.originalStyleSheet)
        self.highlighted = False

    def getScore(self):
        return int(self.ui.teamScore.text())

    def highlight(self):
        self.ui.teamName.setStyleSheet('QLabel {color: red}')
        self.ui.teamScore.setStyleSheet('QLabel {color: red}')
        self.highlighted = True

    def isBonus(self):
        return self.bonus

    def isHighlighted(self):
        return self.highlighted

    def setName(self, name):
        self.ui.teamName.setText(name)
    
    def setScore(self, score):
        self.ui.teamScore.setText(str(score))
