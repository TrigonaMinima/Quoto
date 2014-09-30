from PyQt4 import QtGui, QtCore
from quoto import Ui_Form
import sys


class Quo_win(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Quo_win, self).__init__(parent)
        self.ui = Ui_Form()

        self.ui.setupUi(self)
        self.insert_quote()

    def insert_quote(self):
            self.ui.textBrowser.setHtml("Shivam Rana")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Quo_win()
    window.show()
    sys.exit(app.exec_())
