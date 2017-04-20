from main_gui import Ui_MainWindow
from retrieve_gui import Ui_Dialog
from case_pair_gui import Ui_pair_dialog
from update_case_gui import Ui_update_dia
from delete_gui import Ui_delete_dialog
from new_detective_gui import Ui_new_detective
import sqlite3 as sql
import render
from PyQt4 import QtCore, QtGui
import sys
from dateutil.parser import parse
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
            if CN.isdigit() == False:
                print("Case Number must be a digit")
                return;
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
            if beat.isdigit() and ward.isdigit() and block.isdigit() == False:
                pass
            else:
                print("This parameters are invalid. Beat and Ward are digits while block is a string")
                return;
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
        flag = False
        if case.isdigit() == False and len(case) != 4:
            print('Case numbers are made up of digits rangining with the size of 5.')
        for child in self.ui.groupBox_2.findChildren(QtGui.QRadioButton):
            if child.isChecked():
                where_change = child.text()
                flag = update_win.check_change(change, where_change)
        if case and flag:
            render.update_case(case, change, where_change)
    def check_change(change, where):
        if where == 'Date':
            try:
                parse(change)
                return True
            except ValueError:
                print('A date change must be in date format')
                return False
        elif where == 'Latitude' or where == 'Longitude':
            try:
                float(change)
                return True
            except:
                print('Latitude and Longitude must be a float')
                return False
        elif where == 'Ward' or where == 'Beat':
            try:
                int(change)
                return True
            except:
                print("Ward or Block must be an integer")
                return False
        elif where == 'Domestic' or where == 'Arrest':
            if change == 'True' or change == 'true':
                change = True
                return change
            elif change == 'False' or change == 'false':
                change = False
                return True
            else:
                print('Domestic or Arrest must be entered as True, true, False or false')
                return False
        else:
            try:
                int(change)
                float(change)
                print('A string should be inputted for the value you are trying to change')
                return False
            except:return True
class detective_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_new_detective()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.add_dete)
    def add_dete(self):
        deteID = self.ui.line_detID.text()
        name = self.ui.line_name.text()
        title = self.ui.line_title.text()
        badge = self.ui.line_badge.text()
        station = self.ui.spin_station.value()
        CN = self.ui.line_offCN.text()
        render.create_detective(deteID, name, title, badge, station, CN)
class pair_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_pair_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.make_pair)
    def make_pair(self):
        try:
          CN1 = int(self.ui.line_case_1.text())
          CN2 = int(self.ui.line_case_2.text())
        except:
          print("Case Numbers are digits")
          return;
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
        self.ui.button_off.clicked.connect(self.add_detective)
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
    def add_detective(self):
        self.detective = detective_win()
        self.detective.show()
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    newWin = MyForm()
    newWin.show()
    sys.exit(app.exec_())
