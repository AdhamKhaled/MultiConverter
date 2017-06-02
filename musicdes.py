# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'music.ui'
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

class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(780, 407)
        font = QtGui.QFont()
        font.setPointSize(15)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 90, 91, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Light"))
        font.setPointSize(36)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 101, 91))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Light"))
        font.setPointSize(25)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 461, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(630, 50, 97, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Light"))
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(636, 335, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Yu Gothic UI Light"))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(300, 180, 61, 191))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "to", None))
        self.label_2.setText(_translate("Form", "Path : ", None))
        self.pushButton.setText(_translate("Form", "Browse", None))
        self.pushButton_2.setText(_translate("Form", "Convert ", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "MP3", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "WAV", None))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "AIFF", None))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "FLAC", None))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "OGG", None))
        item = self.listWidget.item(5)
        item.setText(_translate("Form", "M4A", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

