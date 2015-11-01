from PyQt4.QtGui import QWidget, QPixmap
from PyQt4.QtCore import Qt

from Ui_playerwidget import Ui_PlayerWidget

class PlayerWidget(QWidget, Ui_PlayerWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_PlayerWidget()
        self.ui.setupUi(self)

    def resizeEvent (self, event):
        scaledSize = self.originalPicture.size()
        scaledSize.scale(self.ui.playerPicture.size(), Qt.KeepAspectRatio)
        if not self.ui.playerPicture.pixmap() or scaledSize != self.ui.playerPicture.pixmap().size():
            self.updatePicture()

    def newPicture(self, picture):
        self.originalPicture = QPixmap(picture)
        self.updatePicture()

    def updatePicture(self):
        self.ui.playerPicture.setPixmap(self.originalPicture.scaled(self.ui.playerPicture.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def updateWidget(self, picture, name):
        self.newPicture(picture)
        self.ui.playerName.setText(name)
