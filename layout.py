# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
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
        MainWindow.resize(1066, 688)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.gridLayout.addWidget(self.checkBox_4, 7, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout.addWidget(self.lcdNumber, 4, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 5, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.gridLayout.addWidget(self.checkBox_3, 6, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 2)
        self.dial = QtGui.QDial(self.centralwidget)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout.addWidget(self.dial, 5, 1, 3, 1)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1066, 33))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkBox_4.setText(_translate("MainWindow", "Emotion", None))
        self.checkBox_2.setText(_translate("MainWindow", "Landmark", None))
        self.checkBox.setText(_translate("MainWindow", "Detection", None))
        self.pushButton.setText(_translate("MainWindow", "START", None))
        self.checkBox_3.setText(_translate("MainWindow", "Gender", None))
        self.pushButton_2.setText(_translate("MainWindow", "STOP", None))
        self.pushButton_3.setText(_translate("MainWindow", "QUIT", None))
	self.checkBox.setChecked(True)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



