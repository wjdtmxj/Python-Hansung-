# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from transfer import Ui_MainWindow

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

class Ui_Main(object):
    def setupUi(self, Main):
        self.slist=[]
        Main.setObjectName(_fromUtf8("Main"))
        Main.resize(712, 575)
        Main.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:repeat, x1:0.859661, y1:0.744, x2:1, y2:1, stop:0 rgba(0, 54, 255, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))"))
        self.pushButton = QtGui.QPushButton(Main)
        self.pushButton.setGeometry(QtCore.QRect(460, 310, 91, 41))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton.clicked.connect(self.search)
        
        self.lineEdit = QtGui.QLineEdit(Main)
        self.lineEdit.setGeometry(QtCore.QRect(460, 260, 211, 41))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.calendarWidget = QtGui.QCalendarWidget(Main)
        self.calendarWidget.setGeometry(QtCore.QRect(460, 360, 161, 141))
        self.calendarWidget.setStyleSheet(_fromUtf8("\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);"))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.tableWidget = QtGui.QTableWidget(Main)
        self.tableWidget.setGeometry(QtCore.QRect(40, 200, 401, 331))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtGui.QLabel(Main)
        self.label.setGeometry(QtCore.QRect(40, 20, 651, 171))
        self.label.setStyleSheet(_fromUtf8("color: rgb(170, 255, 0);\n"
"border-color: rgb(0, 255, 0);\n"
"gridline-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 127);\n"
"font: 75 18pt \"Aharoni\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(Main)
        self.comboBox.setGeometry(QtCore.QRect(460, 210, 111, 41))
        self.comboBox.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))

        self.searchSubway()
        self.comboBox.currentIndexChanged.connect(self.combobox_click)
        
        self.pushButton_2 = QtGui.QPushButton(Main)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 310, 91, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.transfer)
        

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        Main.setWindowTitle(_translate("Main", "Dialog", None))
        self.pushButton.setText(_translate("Main", "역 검색", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Main", "호선", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Main", "역 이름", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Main", "설치 위치", None))
        self.label.setToolTip(_translate("Main", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(_translate("Main", "\n"
"Welcome\n"
"To\n"
"Subway\n"
"Supporter\n"
"\n"
"S.S\n"
" ", None))
        
        
        self.comboBox.setItemText(0, _translate("Main", "-----선택-----", None))
        self.comboBox.setItemText(1, _translate("Main", "Subway 1", None))
        self.comboBox.setItemText(2, _translate("Main", "Subway 2", None))
        self.comboBox.setItemText(3, _translate("Main", "Subway 3", None))
        self.comboBox.setItemText(4, _translate("Main", "Subway 4", None))
        self.pushButton_2.setText(_translate("Main", "환승역 정보", None))

    def searchSubway(self):
        with open('currunt_elevator.csv') as fo:
            columns = fo.readline()
            self.slist=[line.decode('utf-8').strip().split(",")for line in fo.readlines()]
        self.tableWidget.setRowCount(len(self.slist))
        for i,d in enumerate (self.slist):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem (d[0]))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem (d[1]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem (d[2]))
    
    def combobox_click(self):
        result = self.comboBox.currentText()
        if (result == 'Subway 1'):
            self.changeSubway('1')
        elif (result == 'Subway 2'):
            self.changeSubway('2')
        elif (result == 'Subway 3'):
            self.changeSubway('3')
        elif (result == 'Subway 4'):
            self.changeSubway('4')

    def changeSubway(self,line_num):
        lst = [x for x in self.slist if x[0]==line_num]
        self.tableWidget.setRowCount(len(lst))
        for i,d in enumerate (lst):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem (d[0]))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem (d[1]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem (d[2]))

    def search(self):
        result = self.lineEdit.text()
        find = self.searchSubway()
        lst = [x for x in self.slist if x[1]==unicode(result)]
        self.tableWidget.setRowCount(len(lst))
        for i,d in enumerate (lst):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem (d[0]))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem (d[1]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem (d[2]))

    def transfer(self):
        self.window = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Main = QtGui.QDialog()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

