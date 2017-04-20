# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retrieve_gui.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(472, 356)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.location_tab = QtGui.QTabWidget(Dialog)
        self.location_tab.setObjectName(_fromUtf8("location_tab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 451, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.line_beat = QtGui.QLineEdit(self.frame)
        self.line_beat.setObjectName(_fromUtf8("line_beat"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_beat)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_4)
        self.line_ward = QtGui.QLineEdit(self.frame)
        self.line_ward.setObjectName(_fromUtf8("line_ward"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.line_ward)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_5)
        self.line_block = QtGui.QLineEdit(self.frame)
        self.line_block.setObjectName(_fromUtf8("line_block"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.line_block)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_6)
        self.location_tab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.frame_2 = QtGui.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(13, 13, 331, 131))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.line_case = QtGui.QLineEdit(self.frame_2)
        self.line_case.setGeometry(QtCore.QRect(10, 10, 176, 25))
        self.line_case.setObjectName(_fromUtf8("line_case"))
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(199, 14, 141, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(14, 116, 16, 16))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.checkBox_2 = QtGui.QCheckBox(self.frame_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 291, 23))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.location_tab.addTab(self.tab_2, _fromUtf8(""))
        self.date_tab = QtGui.QWidget()
        self.date_tab.setObjectName(_fromUtf8("date_tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.date_tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_4 = QtGui.QFrame(self.date_tab)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.frame_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtGui.QDateEdit(self.frame_4)
        self.dateEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2015, 12, 31), QtCore.QTime(17, 59, 59)))
        self.dateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2015, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setDate(QtCore.QDate(2015, 1, 1))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtGui.QFrame(self.date_tab)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.checkBox = QtGui.QCheckBox(self.frame_5)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.verticalLayout.addWidget(self.frame_5)
        self.location_tab.addTab(self.date_tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.location_tab)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.location_tab.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_4.setText(_translate("Dialog", "Beat", None))
        self.label_5.setText(_translate("Dialog", "Ward", None))
        self.label_6.setText(_translate("Dialog", "Block", None))
        self.location_tab.setTabText(self.location_tab.indexOf(self.tab), _translate("Dialog", "Location", None))
        self.label_7.setText(_translate("Dialog", "Case Number", None))
        self.checkBox_2.setText(_translate("Dialog", "Map Paired Cases", None))
        self.location_tab.setTabText(self.location_tab.indexOf(self.tab_2), _translate("Dialog", "Incident", None))
        self.label.setText(_translate("Dialog", "Crime Date", None))
        self.checkBox.setText(_translate("Dialog", "Search by Date", None))
        self.location_tab.setTabText(self.location_tab.indexOf(self.date_tab), _translate("Dialog", "Date", None))

