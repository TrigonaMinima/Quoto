import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.text = 'My quote is here...can u see shivam ?......or u want a much bigger box for it!! My quote is here...can u see shivam ?......or u want a much bigger box for it!!'
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


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
