from main_gui import Ui_MainWindow
from retrieve_gui import Ui_Dialog
from case_pair_gui import Ui_pair_dialog
from update_case_gui import Ui_update_dia
import sqlite3 as sql
from PyQt4 import QtCore, QtGui
import sys
import renderByData

class retrieve_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.implement_search)
    def implement_search(self):
        beat = self.ui.line_beat.text()
        ward = self.ui.line_ward.text()
        block = self.ui.line_block.text()
        if beat and ward and block:
            input_loc = [beat, ward, block]
            pass #(Query)
        CN = self.ui.line_case.text()
        if CN != 0:
            pass #Query case number
        date = self.ui.dateEdit.date().getDate()
        input = str(date[1])+"/"+ str(date[2])+"/"+str(date[0])
        print(input)        
        renderByData.render(input)


class update_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_update_dia()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.update_case)
    def update_case(self):
        pass
class pair_win(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_pair_dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.make_pair)
    def make_pair(self):
        pass
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.retrieve_data)
        self.ui.pushButton_2.clicked.connect(self.pair_cases)
        self.ui.pushButton_3.clicked.connect(self.update_data)
    def pair_cases(self):
        self.pair = pair_win()
        self.pair.show()
    def retrieve_data(self):
        self.retrieve = retrieve_win()
        self.retrieve.show()
    def update_data(self):
        self.update = update_win()
        self.update.show()
    def delete_case(self):
        pass
if __name__ == "__main__":
    app= QtGui.QApplication(sys.argv)
    newWin = MyForm()
    newWin.show()
    sys.exit(app.exec_())
