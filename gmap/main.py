from main_gui import Ui_MainWindow
from retrieve_gui import Ui_Dialog
from case_pair_gui import Ui_pair_dialog
from update_case_gui import Ui_update_dia
from delete_gui import Ui_delete_dialog
import sqlite3 as sql
import render
from PyQt4 import QtCore, QtGui
import sys
class retrieve_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.implement_search)
    def implement_search(self):
        CN = self.ui.line_case.text()
        pair = self.ui.checkBox_2.isChecked()
        if CN != '':
            if pair:
                render.render('CNPair', CN)
            else:render.render('CN',CN)
            return;
        beat = self.ui.line_beat.text()
        ward = self.ui.line_ward.text()
        block = self.ui.line_block.text()
        date = self.ui.dateEdit.date().getDate()
        input = str(date[1])+"/"+ str(date[2])+"/"+str(date[0])
        if beat and ward and block:
            if self.ui.checkBox.isChecked():
                input_loc = [beat, ward, block, input]
                render.render('DateLocation', input_loc)
            else:
                input_loc = [beat, ward, block]
                render.render('Location', input_loc)
            return;
        if self.ui.checkBox and date:
            render.render('Date', input)
class update_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_update_dia()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.update_case)
    def update_case(self):
        case = self.ui.lineEdit.text()
        change = self.ui.lineEdit_2.text()
        for child in self.ui.groupBox_2.findChildren(QtGui.QRadioButton):
            if child.isChecked():
                where_change = child.text()
        if case and change and where_change:
            pass
            render.update_case(case, change, where_change)
class pair_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_pair_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.make_pair)
    def make_pair(self):
        CN1 = int(self.ui.line_case_1.text())
        CN2 = int(self.ui.line_case_2.text())
        description = self.ui.lineEdit.text()
        if CN1 and CN2 and description:
            render.pair_cases(CN1, CN2, description)
class delete_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_delete_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.delete_case)
    def delete_case(self):
        CN = self.ui.line_delete.text()
        if  CN != '':
            render.delete_case(CN)
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.find_button.clicked.connect(self.retrieve_data)
        self.ui.pair_button.clicked.connect(self.pair_cases)
        self.ui.button_update.clicked.connect(self.update_data)
        self.ui.button_del.clicked.connect(self.delete_data)
    def pair_cases(self):
        self.pair = pair_win()
        self.pair.show()
    def retrieve_data(self):
        self.retrieve = retrieve_win()
        self.retrieve.show()
    def update_data(self):
        self.update = update_win()
        self.update.show()
    def delete_data(self):
        self.delete_w = delete_win()
        self.delete_w.show()
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    newWin = MyForm()
    newWin.show()
    sys.exit(app.exec_())
