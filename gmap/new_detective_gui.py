# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_detective_gui.ui'
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

class Ui_new_detective(object):
    def setupUi(self, new_detective):
        new_detective.setObjectName(_fromUtf8("new_detective"))
        new_detective.resize(453, 291)
        self.verticalLayout = QtGui.QVBoxLayout(new_detective)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(new_detective)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.line_detID = QtGui.QLineEdit(self.frame)
        self.line_detID.setObjectName(_fromUtf8("line_detID"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.line_detID)
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.label)
        self.line_title = QtGui.QLineEdit(self.frame)
        self.line_title.setObjectName(_fromUtf8("line_title"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.line_title)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_3)
        self.line_badge = QtGui.QLineEdit(self.frame)
        self.line_badge.setObjectName(_fromUtf8("line_badge"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.line_badge)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.label_4)
        self.spin_station = QtGui.QSpinBox(self.frame)
        self.spin_station.setMinimum(0)
        self.spin_station.setProperty("value", 5)
        self.spin_station.setObjectName(_fromUtf8("spin_station"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.spin_station)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.label_5)
        self.line_offCN = QtGui.QLineEdit(self.frame)
        self.line_offCN.setObjectName(_fromUtf8("line_offCN"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.line_offCN)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_2)
        self.line_name = QtGui.QLineEdit(self.frame)
        self.line_name.setObjectName(_fromUtf8("line_name"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.line_name)
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label_6)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(new_detective)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(new_detective)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), new_detective.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), new_detective.reject)
        QtCore.QMetaObject.connectSlotsByName(new_detective)

    def retranslateUi(self, new_detective):
        new_detective.setWindowTitle(_translate("new_detective", "Dialog", None))
        self.label.setText(_translate("new_detective", "DetectiveID", None))
        self.label_3.setText(_translate("new_detective", "Title", None))
        self.label_4.setText(_translate("new_detective", "Badge Id", None))
        self.spin_station.setPrefix(_translate("new_detective", "0", None))
        self.label_5.setText(_translate("new_detective", "Station", None))
        self.label_2.setText(_translate("new_detective", "CN", None))
        self.label_6.setText(_translate("new_detective", "Name", None))

