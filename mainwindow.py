# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hi.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1100, 707)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(580, 60, 371, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(580, 130, 371, 41))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(580, 200, 371, 41))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(590, 470, 96, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(590, 500, 96, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(590, 530, 96, 20))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(590, 560, 96, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(800, 470, 111, 31))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(810, 520, 101, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(580, 260, 361, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 33))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "START", None))
        self.pushButton_2.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_3.setText(_translate("MainWindow", "QUIT", None))
        self.checkBox.setText(_translate("MainWindow", "Detection", None))
        self.checkBox_2.setText(_translate("MainWindow", "Landmark", None))
        self.checkBox_3.setText(_translate("MainWindow", "Gender", None))
        self.checkBox_4.setText(_translate("MainWindow", "Emotion", None))
	self.checkBox_2.setChecked(True)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


