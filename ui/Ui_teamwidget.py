# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Justin\qbscore\ui\teamwidget.ui'
#
# Created: Mon Mar 04 04:16:58 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TeamWidget(object):
    def setupUi(self, TeamWidget):
        TeamWidget.setObjectName(_fromUtf8("TeamWidget"))
        TeamWidget.resize(295, 319)
        self.MainLayout = QtGui.QVBoxLayout(TeamWidget)
        self.MainLayout.setObjectName(_fromUtf8("MainLayout"))
        self.teamLayout = QtGui.QVBoxLayout()
        self.teamLayout.setObjectName(_fromUtf8("teamLayout"))
        self.teamName = QtGui.QLabel(TeamWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.teamName.setFont(font)
        self.teamName.setText(_fromUtf8(""))
        self.teamName.setScaledContents(True)
        self.teamName.setAlignment(QtCore.Qt.AlignCenter)
        self.teamName.setWordWrap(True)
        self.teamName.setObjectName(_fromUtf8("teamName"))
        self.teamLayout.addWidget(self.teamName)
        self.teamScore = QtGui.QLabel(TeamWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.teamScore.setFont(font)
        self.teamScore.setText(_fromUtf8(""))
        self.teamScore.setAlignment(QtCore.Qt.AlignCenter)
        self.teamScore.setObjectName(_fromUtf8("teamScore"))
        self.teamLayout.addWidget(self.teamScore)
        self.MainLayout.addLayout(self.teamLayout)

        self.retranslateUi(TeamWidget)
        QtCore.QMetaObject.connectSlotsByName(TeamWidget)

    def retranslateUi(self, TeamWidget):
        TeamWidget.setWindowTitle(QtGui.QApplication.translate("TeamWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TeamWidget = QtGui.QWidget()
    ui = Ui_TeamWidget()
    ui.setupUi(TeamWidget)
    TeamWidget.show()
    sys.exit(app.exec_())

