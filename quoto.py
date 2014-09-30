# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/quoto.ui'
#
# Created: Tue Sep 30 15:50:31 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(648, 120)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setLocale(
            QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
        self.textBrowser.setFrameShape(QtGui.QFrame.Panel)
        self.textBrowser.setFrameShadow(QtGui.QFrame.Raised)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setTextInteractionFlags(
            QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Quoto - Daily Quote", None))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-\
                                 //W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html\
                                 40/strict.dtd\">\n""<html><head><meta name=\"qrichtext\" \
                                 content=\"1\" /><style type=\"text/css\">\n""p, li { white-space: \
                                 pre-wrap; }\n""</style></head><body style=\" font-family:\'Ubuntu\'; \
                                 font-size:12pt; font-weight:400; font-style:normal;\">\n""<p \
                                 align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; \
                                 margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; \
                                 text-indent:0px;\"><br /></p></body></html>", None))
