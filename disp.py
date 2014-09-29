from PyQt4 import QtGui, QtCore
from quoto import Ui_Form
import sys


class Quo_win(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Quo_win, self).__init__(parent)
        self.ui = Ui_Form()
	self.initUI()
        self.ui.text = 'sdsjhdks'
        self.show()
    
    def initUI(self):
        self.text = 'My Quote is here!!! works for any size of string ..yippee!!!'
        if (len(self.text) < 48):
            self.setGeometry(300, 300, 280, 170)
        else :
            n= len(self.text)
            l = n/2
            self.text=self.text[:l]+'\n'+self.text[l:]
            self.setGeometry(300, 300, 280+3*len(self.text) + 10, 170)
        self.setWindowTitle('Daily Quote')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()

    def drawText(self, event, qp):

        qp.setPen(QtGui.QColor(0, 0, 0))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Quo_win()
    sys.exit(app.exec_())
