# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\a_codes\pycharm\BlogChinaCollector\mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QDialog, QLabel, QGridLayout, QHBoxLayout
from spider import get, to_txt
from word_cloud_test import form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        from PyQt5.QtWidgets import QApplication, QWidget
        # 获取桌面大小
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

        # 添加组件
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect((self.width-111)/3, 20, 111, 41))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect((self.width - 111) * 2 / 3, 20, 111, 41))
        self.pushButton2.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 70, self.width-60, self.height - 150 - 41))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 914, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.updateUi()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "博客园收集工具 v1.0"))
        self.pushButton1.setText(_translate("MainWindow", "更新一下！"))
        self.pushButton2.setText(_translate("MainWindow", "分析一下！"))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "文章"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "链接"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "作者"))
        self.pushButton1.clicked.connect(self.updateUi)
        self.pushButton2.clicked.connect(self.showdialog)

    def updateUi(self):
        data = get()
        to_txt()
        for i in range(len(data['title'])):
            itemContent1 = QTableWidgetItem(data['title'][i])
            itemContent2 = QTableWidgetItem(data['link'][i])
            itemContent3 = QTableWidgetItem(data['writer'][i])
            self.tableWidget.setItem(i,0,itemContent1)
            self.tableWidget.setItem(i,1,itemContent2)
            self.tableWidget.setItem(i,2,itemContent3)

    def showdialog(self):
        form()
        self.dialog = my_dialog()
        self.dialog.show()
        self.dialog.exec_()

class my_dialog(QDialog):
    def __init__(self,parent = None):
        super(my_dialog, self).__init__(parent)

        hbox = QHBoxLayout (self)

        # 设置对话框的标题及大小
        self.setWindowTitle('词云分析')
        self.label = QLabel()
        self.label.resize(1200, 800)
        self.resize(1200,800)
        self.pix = QPixmap('B_word.jpg').scaled(self.label.width(), self.label.height())
        self.label.setPixmap(self.pix)
        self.label.setScaledContents(True)
        hbox.addWidget(self.label)
        self.setLayout(hbox)