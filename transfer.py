# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transfer.ui'
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
        MainWindow.resize(633, 496)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 127);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 420, 351, 41))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 420, 111, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton_2.clicked.connect(self.search)
        
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 591, 381))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)

        self.searchTransfer()
        
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_2.setText(_translate("MainWindow", "환승역 정보 검색", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "호선", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "역명", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "환승노선", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "환승소요시간", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "빠른환승", None))

    def searchTransfer(self):
        with open('transfer2.csv') as fo:
            columns = fo.readline()
            self.slist=[line.decode('utf-8').strip().split(",")for line in fo.readlines()]
        self.tableWidget.setRowCount(len(self.slist))
        for i,d in enumerate (self.slist):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem (d[0]))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem (d[1]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem (d[2]))
            self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem (d[3]))
            self.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem (d[4]))

    def search(self):
        result = self.lineEdit.text()
        find = self.searchTransfer()
        lst = [x for x in self.slist if x[1]==unicode(result)]
        self.tableWidget.setRowCount(len(lst))
        for i,d in enumerate (lst):
            self.tableWidget.setItem(i, 0, QtGui.QTableWidgetItem (d[0]))
            self.tableWidget.setItem(i, 1, QtGui.QTableWidgetItem (d[1]))
            self.tableWidget.setItem(i, 2, QtGui.QTableWidgetItem (d[2]))
            self.tableWidget.setItem(i, 3, QtGui.QTableWidgetItem (d[3]))
            self.tableWidget.setItem(i, 4, QtGui.QTableWidgetItem (d[4]))
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

