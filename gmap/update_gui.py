# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_case_gui.ui'
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

class Ui_update_dia(object):
    def setupUi(self, update_dia):
        update_dia.setObjectName(_fromUtf8("update_dia"))
        update_dia.resize(400, 404)
        self.verticalLayout = QtGui.QVBoxLayout(update_dia)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(update_dia)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout = QtGui.QFormLayout(self.frame)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.line_case_num = QtGui.QLineEdit(self.frame)
        self.line_case_num.setObjectName(_fromUtf8("line_case_num"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.line_case_num)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.line_change = QtGui.QLineEdit(self.frame)
        self.line_change.setObjectName(_fromUtf8("line_change"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.line_change)
        self.verticalLayout.addWidget(self.frame)
        self.groupBox_2 = QtGui.QGroupBox(update_dia)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioButton_9 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.gridLayout.addWidget(self.radioButton_9, 6, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.gridLayout.addWidget(self.radioButton, 0, 0, 4, 4)
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.gridLayout.addWidget(self.radioButton_4, 1, 2, 1, 4)
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.gridLayout.addWidget(self.radioButton_7, 5, 2, 1, 1)
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.gridLayout.addWidget(self.radioButton_5, 6, 2, 1, 1)
        self.radioButton_8 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.gridLayout.addWidget(self.radioButton_8, 7, 0, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.gridLayout.addWidget(self.radioButton_2, 5, 0, 1, 1)
        self.radioButton_10 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.gridLayout.addWidget(self.radioButton_10, 4, 2, 1, 1)
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.gridLayout.addWidget(self.radioButton_3, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(update_dia)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(update_dia)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), update_dia.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), update_dia.reject)
        QtCore.QMetaObject.connectSlotsByName(update_dia)

    def retranslateUi(self, update_dia):
        update_dia.setWindowTitle(_translate("update_dia", "Dialog", None))
        self.label.setText(_translate("update_dia", "Case Number:", None))
        self.label_2.setText(_translate("update_dia", "Change:", None))
        self.groupBox_2.setTitle(_translate("update_dia", "What to Change", None))
        self.radioButton_9.setText(_translate("update_dia", "Latitude", None))
        self.radioButton.setText(_translate("update_dia", "Date", None))
        self.radioButton_4.setText(_translate("update_dia", "Block", None))
        self.radioButton_7.setText(_translate("update_dia", "Ward", None))
        self.radioButton_5.setText(_translate("update_dia", "Primary Description", None))
        self.radioButton_8.setText(_translate("update_dia", "Longitude", None))
        self.radioButton_2.setText(_translate("update_dia", "Arrest", None))
        self.radioButton_10.setText(_translate("update_dia", "Beat", None))
        self.radioButton_3.setText(_translate("update_dia", "Domestic", None))

