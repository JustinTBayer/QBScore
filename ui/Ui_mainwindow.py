# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Justin\code\qbscore\qbscore 2 bonus mode\QBScore\ui\mainwindow.ui'
#
# Created: Sat Nov 07 15:20:30 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem2)
        self.informationLayout = QtGui.QHBoxLayout()
        self.informationLayout.setObjectName(_fromUtf8("informationLayout"))
        self.tournamentLabel = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tournamentLabel.sizePolicy().hasHeightForWidth())
        self.tournamentLabel.setSizePolicy(sizePolicy)
        self.tournamentLabel.setText(_fromUtf8(""))
        self.tournamentLabel.setObjectName(_fromUtf8("tournamentLabel"))
        self.informationLayout.addWidget(self.tournamentLabel)
        self.roundLabel = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roundLabel.sizePolicy().hasHeightForWidth())
        self.roundLabel.setSizePolicy(sizePolicy)
        self.roundLabel.setText(_fromUtf8(""))
        self.roundLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.roundLabel.setObjectName(_fromUtf8("roundLabel"))
        self.informationLayout.addWidget(self.roundLabel)
        self.mainLayout.addLayout(self.informationLayout)
        self.buzzedLayout = QtGui.QHBoxLayout()
        self.buzzedLayout.setSpacing(0)
        self.buzzedLayout.setObjectName(_fromUtf8("buzzedLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.buzzedLayout.addItem(spacerItem3)
        self.playerWidgetLayout = QtGui.QVBoxLayout()
        self.playerWidgetLayout.setSpacing(0)
        self.playerWidgetLayout.setObjectName(_fromUtf8("playerWidgetLayout"))
        self.buzzedLayout.addLayout(self.playerWidgetLayout)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.buzzedLayout.addItem(spacerItem4)
        self.mainLayout.addLayout(self.buzzedLayout)
        self.teamsLayout = QtGui.QHBoxLayout()
        self.teamsLayout.setSpacing(0)
        self.teamsLayout.setObjectName(_fromUtf8("teamsLayout"))
        self.team1Layout = QtGui.QVBoxLayout()
        self.team1Layout.setObjectName(_fromUtf8("team1Layout"))
        self.teamsLayout.addLayout(self.team1Layout)
        self.lcdTimer = QtGui.QLCDNumber(self.centralWidget)
        self.lcdTimer.setObjectName(_fromUtf8("lcdTimer"))
        self.teamsLayout.addWidget(self.lcdTimer)
        self.team2Layout = QtGui.QVBoxLayout()
        self.team2Layout.setObjectName(_fromUtf8("team2Layout"))
        self.teamsLayout.addLayout(self.team2Layout)
        self.mainLayout.addLayout(self.teamsLayout)
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.mainLayout.addItem(spacerItem5)
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 1)
        self.mainLayout.setStretch(2, 10)
        self.mainLayout.setStretch(3, 1)
        self.mainLayout.setStretch(4, 1)
        self.gridLayout.addLayout(self.mainLayout, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

