from PyQt4 import QtGui, uic
import sys


class win(QtGui.QMainWindow):

    def __init__(self):
        super(win, self).__init__()
        uic.loadUi('GUI/quoto.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = win()
    sys.exit(app.exec_())
