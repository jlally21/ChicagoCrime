# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
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
        MainWindow.resize(800, 396)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Stencil"))
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.find_button = QtGui.QPushButton(self.frame)
        self.find_button.setObjectName(_fromUtf8("find_button"))
        self.horizontalLayout.addWidget(self.find_button)
        self.pair_button = QtGui.QPushButton(self.frame)
        self.pair_button.setObjectName(_fromUtf8("pair_button"))
        self.horizontalLayout.addWidget(self.pair_button)
        self.button_off = QtGui.QPushButton(self.frame)
        self.button_off.setObjectName(_fromUtf8("button_off"))
        self.horizontalLayout.addWidget(self.button_off)
        self.button_update = QtGui.QPushButton(self.frame)
        self.button_update.setObjectName(_fromUtf8("button_update"))
        self.horizontalLayout.addWidget(self.button_update)
        self.button_del = QtGui.QPushButton(self.frame)
        self.button_del.setObjectName(_fromUtf8("button_del"))
        self.horizontalLayout.addWidget(self.button_del)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRead_Me = QtGui.QAction(MainWindow)
        self.actionRead_Me.setObjectName(_fromUtf8("actionRead_Me"))
        self.menuFile.addAction(self.actionRead_Me)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Chicago Homicide Tool ", None))
        self.find_button.setText(_translate("MainWindow", "Find and Map Cases", None))
        self.pair_button.setText(_translate("MainWindow", "Pair Cases", None))
        self.button_off.setText(_translate("MainWindow", "Add Officer", None))
        self.button_update.setText(_translate("MainWindow", "Update Data", None))
        self.button_del.setText(_translate("MainWindow", "Delete Case", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionRead_Me.setText(_translate("MainWindow", "Read Me", None))

