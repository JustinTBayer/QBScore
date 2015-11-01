# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Justin\code\qbscore\qbscore 2 bonus mode\ui\moderatorwindow.ui'
#
# Created: Sat Oct 31 17:41:13 2015
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
        MainWindow.resize(777, 599)
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Question = QtGui.QTextBrowser(self.widget)
        self.Question.setObjectName(_fromUtf8("Question"))
        self.verticalLayout.addWidget(self.Question)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.Team = QtGui.QLabel(self.widget)
        self.Team.setObjectName(_fromUtf8("Team"))
        self.verticalLayout_2.addWidget(self.Team)
        self.Name = QtGui.QLabel(self.widget)
        self.Name.setObjectName(_fromUtf8("Name"))
        self.verticalLayout_2.addWidget(self.Name)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.Answer = QtGui.QTextEdit(self.widget)
        self.Answer.setObjectName(_fromUtf8("Answer"))
        self.horizontalLayout_2.addWidget(self.Answer)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.Power = QtGui.QPushButton(self.widget)
        self.Power.setObjectName(_fromUtf8("Power"))
        self.verticalLayout_3.addWidget(self.Power)
        self.Correct = QtGui.QPushButton(self.widget)
        self.Correct.setObjectName(_fromUtf8("Correct"))
        self.verticalLayout_3.addWidget(self.Correct)
        self.Negative = QtGui.QPushButton(self.widget)
        self.Negative.setObjectName(_fromUtf8("Negative"))
        self.verticalLayout_3.addWidget(self.Negative)
        self.Clear = QtGui.QPushButton(self.widget)
        self.Clear.setObjectName(_fromUtf8("Clear"))
        self.verticalLayout_3.addWidget(self.Clear)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.Correct_Answer = QtGui.QPushButton(self.widget)
        self.Correct_Answer.setObjectName(_fromUtf8("Correct_Answer"))
        self.verticalLayout_6.addWidget(self.Correct_Answer)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_6.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.Previous = QtGui.QPushButton(self.widget)
        self.Previous.setObjectName(_fromUtf8("Previous"))
        self.verticalLayout_4.addWidget(self.Previous)
        self.Next = QtGui.QPushButton(self.widget)
        self.Next.setObjectName(_fromUtf8("Next"))
        self.verticalLayout_4.addWidget(self.Next)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.actionNew_Game = QtGui.QAction(MainWindow)
        self.actionNew_Game.setObjectName(_fromUtf8("actionNew_Game"))
        self.menuFile.addAction(self.actionNew_Game)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.Team.setText(QtGui.QApplication.translate("MainWindow", "Team", None, QtGui.QApplication.UnicodeUTF8))
        self.Name.setText(QtGui.QApplication.translate("MainWindow", "Player", None, QtGui.QApplication.UnicodeUTF8))
        self.Power.setText(QtGui.QApplication.translate("MainWindow", "Power (3)", None, QtGui.QApplication.UnicodeUTF8))
        self.Correct.setText(QtGui.QApplication.translate("MainWindow", "Correct (2)", None, QtGui.QApplication.UnicodeUTF8))
        self.Negative.setText(QtGui.QApplication.translate("MainWindow", "Wrong (1)", None, QtGui.QApplication.UnicodeUTF8))
        self.Clear.setText(QtGui.QApplication.translate("MainWindow", "Clear (0)", None, QtGui.QApplication.UnicodeUTF8))
        self.Correct_Answer.setText(QtGui.QApplication.translate("MainWindow", "Change Answer (4)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Timer (5)", None, QtGui.QApplication.UnicodeUTF8))
        self.Previous.setText(QtGui.QApplication.translate("MainWindow", "Previous (6)", None, QtGui.QApplication.UnicodeUTF8))
        self.Next.setText(QtGui.QApplication.translate("MainWindow", "Next (7)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Game.setText(QtGui.QApplication.translate("MainWindow", "New Game", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

