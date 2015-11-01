# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Justin\qbscore\ui\playerwidget.ui'
#
# Created: Tue Mar 05 00:10:03 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PlayerWidget(object):
    def setupUi(self, PlayerWidget):
        PlayerWidget.setObjectName(_fromUtf8("PlayerWidget"))
        PlayerWidget.resize(400, 300)
        self.verticalLayout_2 = QtGui.QVBoxLayout(PlayerWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.playerPicture = QtGui.QLabel(PlayerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerPicture.sizePolicy().hasHeightForWidth())
        self.playerPicture.setSizePolicy(sizePolicy)
        self.playerPicture.setMinimumSize(QtCore.QSize(1, 1))
        self.playerPicture.setText(_fromUtf8(""))
        self.playerPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.playerPicture.setObjectName(_fromUtf8("playerPicture"))
        self.verticalLayout_2.addWidget(self.playerPicture)
        self.playerName = QtGui.QLabel(PlayerWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerName.sizePolicy().hasHeightForWidth())
        self.playerName.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.playerName.setFont(font)
        self.playerName.setText(_fromUtf8(""))
        self.playerName.setAlignment(QtCore.Qt.AlignCenter)
        self.playerName.setObjectName(_fromUtf8("playerName"))
        self.verticalLayout_2.addWidget(self.playerName)

        self.retranslateUi(PlayerWidget)
        QtCore.QMetaObject.connectSlotsByName(PlayerWidget)

    def retranslateUi(self, PlayerWidget):
        PlayerWidget.setWindowTitle(QtGui.QApplication.translate("PlayerWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PlayerWidget = QtGui.QWidget()
    ui = Ui_PlayerWidget()
    ui.setupUi(PlayerWidget)
    PlayerWidget.show()
    sys.exit(app.exec_())

