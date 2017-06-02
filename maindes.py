# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Form.resize(780, 407)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 202, 202))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(35)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8(" background-color: cyan;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:100px;\n"
" max-width:200    px;\n"
" max-height:200px;\n"
" min-width:200px;\n"
" min-height:200px;"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 120, 202, 202))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(35)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_fromUtf8(" background-color: rgb(255, 102, 55);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:100px;\n"
" max-width:200    px;\n"
" max-height:200px;\n"
" min-width:200px;\n"
" min-height:200px;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 120, 202, 202))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Gothic L"))
        font.setPointSize(35)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_fromUtf8(" background-color: rgb(255, 248, 26);\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:100px;\n"
" max-width:200    px;\n"
" max-height:200px;\n"
" min-width:200px;\n"
" min-height:200px;"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Music", None))
        self.pushButton_2.setText(_translate("Form", "Video", None))
        self.pushButton_3.setText(_translate("Form", "Doc.", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

