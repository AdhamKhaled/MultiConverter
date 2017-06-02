from PyQt4 import QtCore, QtGui
from maindes import Ui_Form
from musicdes import Ui_Form1
from videos import Ui_Form2
import sys
import os
class main(QtGui.QWidget,Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.HandleM)
        self.pushButton_2.clicked.connect(self.HandleV)
        self.window2 = None
        self.window3 = None
    def HandleM(self):
        if self.window2 is None:
            self.window2 = Music()
        self.window2.show()
    def HandleV(self):
        if self.window3 is None:
            self.window3 = Videos()
        self.window3.show()

class Music(QtGui.QWidget,Ui_Form1):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.convert)
    def selectFile(self):
            self.dialog = QtGui.QFileDialog #.getOpenFileName()
            self.lineEdit.setText(self.dialog.getOpenFileName(self,'Open File', '', 'Supported Media (*.mp3 *.wav *.ogg *.aiff *.flac *.m4a *.mp4 *.avi *.mkv *.mov)'))
            self.path = self.lineEdit.text()
            self.basefile = os.path.basename(self.path)
            self.patho = self.path.replace(self.basefile,"")
            self.filename, self.ext = os.path.splitext(self.basefile)
            print(self.filename)
            self.ext = self.ext.replace(".", "")
            print(self.ext)
    def convert(self):
        try:
            ext2 = self.listWidget.currentItem().text() 
            if ext2.lower() == self.ext:
                QtGui.QMessageBox.critical(self, "Same file type", "The chosen file is already %s file please choose another file type"%(ext2))
            else :
                cmd = ("ffmpeg -i %s %s"%(self.path,self.patho+self.filename+"."+(ext2).lower()))
                print(cmd)
                os.system(cmd)
        except :
            QtGui.QMessageBox.critical(self, "Choose a file type", "Please choose a file type to convert")
class Videos(QtGui.QWidget,Ui_Form2):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.selectFile)
        self.pushButton_2.clicked.connect(self.convert)
    def selectFile(self):
        self.dialog = QtGui.QFileDialog #.getOpenFileName()
        self.lineEdit.setText(self.dialog.getOpenFileName(self,'Open File', '', 'Supported Media (*.mp4 *.avi *.mov *.mkv)'))
        self.path = self.lineEdit.text()
        self.basefile = os.path.basename(self.path)
        self.patho = self.path.replace(self.basefile,"")
        self.filename, self.ext = os.path.splitext(self.basefile)
        print(self.filename)
        self.ext = self.ext.replace(".", "")
        print(self.ext)
    def convert(self):
        try:
            ext2 = self.listWidget.currentItem().text() 
            if ext2.lower() == self.ext:
                QtGui.QMessageBox.critical(self, "Same file type", "The chosen file is already %s file please choose another file type"%(ext2))
            else :
                cmd = ("ffmpeg -i %s %s"%(self.path,self.patho+self.filename+"."+(ext2).lower()))
                print(cmd)
                os.system(cmd)
        except :
            QtGui.QMessageBox.critical(self, "Choose a file type", "Please choose a file type to convert")



app = QtGui.QApplication(sys.argv)
window = main()
window.show()
app.exec_()
