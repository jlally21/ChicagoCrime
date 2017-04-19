# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'case_pair_gui.ui'
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

class Ui_pair_dialog(object):
    def setupUi(self, pair_dialog):
        pair_dialog.setObjectName(_fromUtf8("pair_dialog"))
        pair_dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(pair_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(pair_dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.line_case_1 = QtGui.QLineEdit(self.frame)
        self.line_case_1.setObjectName(_fromUtf8("line_case_1"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_case_1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.line_case_2 = QtGui.QLineEdit(self.frame)
        self.line_case_2.setObjectName(_fromUtf8("line_case_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_case_2)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(pair_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(pair_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), pair_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), pair_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(pair_dialog)

    def retranslateUi(self, pair_dialog):
        pair_dialog.setWindowTitle(_translate("pair_dialog", "Dialog", None))
        self.label.setText(_translate("pair_dialog", "Case 1:", None))
        self.label_2.setText(_translate("pair_dialog", "Case 2:", None))
        self.label_3.setText(_translate("pair_dialog", "Description", None))

