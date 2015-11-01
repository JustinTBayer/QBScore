from PyQt4 import QtCore,  QtGui,  QtSql
from moderatorwindow import ModeratorWindow

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = ModeratorWindow()
    ui.show()
    sys.exit(app.exec_())
