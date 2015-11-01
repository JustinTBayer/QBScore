# -*- coding: utf-8 -*-

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature, Qt,  SIGNAL
import  mainwindow

from ui.Ui_newgame import Ui_Dialog

class NewGameDialog(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
