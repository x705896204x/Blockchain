# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'companies.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Companies(object):
    def setupUi(self, Companies):
        Companies.setObjectName("Companies")
        Companies.resize(500, 540)
        self.centralwidget = QtWidgets.QWidget(Companies)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 150, 500, 471))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_info = QtWidgets.QWidget()
        self.pg_info.setObjectName("pg_info")
        self.table_info_bor = QtWidgets.QTableWidget(self.pg_info)
        self.table_info_bor.setGeometry(QtCore.QRect(85, 40, 330, 90))
        self.table_info_bor.setObjectName("table_info_bor")
        self.table_info_bor.setColumnCount(0)
        self.table_info_bor.setRowCount(0)
        self.table_info_lent = QtWidgets.QTableWidget(self.pg_info)
        self.table_info_lent.setGeometry(QtCore.QRect(85, 190, 330, 90))
        self.table_info_lent.setObjectName("table_info_lent")
        self.table_info_lent.setColumnCount(0)
        self.table_info_lent.setRowCount(0)
        self.lb_borrowed = QtWidgets.QLabel(self.pg_info)
        self.lb_borrowed.setGeometry(QtCore.QRect(215, 10, 70, 20))
        self.lb_borrowed.setObjectName("lb_borrowed")
        self.lb_lent = QtWidgets.QLabel(self.pg_info)
        self.lb_lent.setGeometry(QtCore.QRect(235, 160, 30, 20))
        self.lb_lent.setObjectName("lb_lent")
        self.stackedWidget.addWidget(self.pg_info)
        self.pg_trans = QtWidgets.QWidget()
        self.pg_trans.setObjectName("pg_trans")
        self.btn_submit_trans = QtWidgets.QPushButton(self.pg_trans)
        self.btn_submit_trans.setGeometry(QtCore.QRect(130, 330, 93, 28))
        self.btn_submit_trans.setObjectName("btn_submit_trans")
        self.btn_reset_trans = QtWidgets.QPushButton(self.pg_trans)
        self.btn_reset_trans.setGeometry(QtCore.QRect(270, 330, 93, 28))
        self.btn_reset_trans.setObjectName("btn_reset_trans")
        self.layoutWidget = QtWidgets.QWidget(self.pg_trans)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 250, 331, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lb_amount_trans = QtWidgets.QLabel(self.layoutWidget)
        self.lb_amount_trans.setObjectName("lb_amount_trans")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_amount_trans)
        self.line_trans_amt = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_trans_amt.setObjectName("line_trans_amt")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_trans_amt)
        self.lb_date_trans = QtWidgets.QLabel(self.layoutWidget)
        self.lb_date_trans.setObjectName("lb_date_trans")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_date_trans)
        self.transfer_date = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.transfer_date.setReadOnly(False)
        self.transfer_date.setObjectName("transfer_date")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.transfer_date)
        self.table_trans_lent = QtWidgets.QTableWidget(self.pg_trans)
        self.table_trans_lent.setGeometry(QtCore.QRect(80, 140, 330, 90))
        self.table_trans_lent.setObjectName("table_trans_lent")
        self.table_trans_lent.setColumnCount(0)
        self.table_trans_lent.setRowCount(0)
        self.lb_lent_2 = QtWidgets.QLabel(self.pg_trans)
        self.lb_lent_2.setGeometry(QtCore.QRect(230, 120, 30, 20))
        self.lb_lent_2.setObjectName("lb_lent_2")
        self.table_trans_bor = QtWidgets.QTableWidget(self.pg_trans)
        self.table_trans_bor.setGeometry(QtCore.QRect(80, 20, 330, 90))
        self.table_trans_bor.setObjectName("table_trans_bor")
        self.table_trans_bor.setColumnCount(0)
        self.table_trans_bor.setRowCount(0)
        self.lb_borrowed_2 = QtWidgets.QLabel(self.pg_trans)
        self.lb_borrowed_2.setGeometry(QtCore.QRect(210, 0, 70, 20))
        self.lb_borrowed_2.setObjectName("lb_borrowed_2")
        self.stackedWidget.addWidget(self.pg_trans)
        self.pg_pur = QtWidgets.QWidget()
        self.pg_pur.setObjectName("pg_pur")
        self.label_2 = QtWidgets.QLabel(self.pg_pur)
        self.label_2.setGeometry(QtCore.QRect(215, 10, 70, 20))
        self.label_2.setObjectName("label_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.pg_pur)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 40, 331, 118))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setHorizontalSpacing(30)
        self.formLayout_3.setVerticalSpacing(20)
        self.formLayout_3.setObjectName("formLayout_3")
        self.lb_from_pur = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_from_pur.setObjectName("lb_from_pur")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_from_pur)
        self.line_pur_from = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_pur_from.setObjectName("line_pur_from")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_pur_from)
        self.lb_amount_pur = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_amount_pur.setObjectName("lb_amount_pur")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_amount_pur)
        self.line_pur_amt = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_pur_amt.setObjectName("line_pur_amt")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_pur_amt)
        self.lb_date_pur = QtWidgets.QLabel(self.layoutWidget1)
        self.lb_date_pur.setObjectName("lb_date_pur")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lb_date_pur)
        self.purchase_date = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        self.purchase_date.setReadOnly(False)
        self.purchase_date.setObjectName("purchase_date")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.purchase_date)
        self.layoutWidget2 = QtWidgets.QWidget(self.pg_pur)
        self.layoutWidget2.setGeometry(QtCore.QRect(100, 180, 278, 30))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(90)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_submit_pur = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_submit_pur.setObjectName("btn_submit_pur")
        self.horizontalLayout_4.addWidget(self.btn_submit_pur)
        self.btn_reset_pur = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_reset_pur.setObjectName("btn_reset_pur")
        self.horizontalLayout_4.addWidget(self.btn_reset_pur)
        self.stackedWidget.addWidget(self.pg_pur)
        self.pg_finance = QtWidgets.QWidget()
        self.pg_finance.setObjectName("pg_finance")
        self.label = QtWidgets.QLabel(self.pg_finance)
        self.label.setGeometry(QtCore.QRect(185, 10, 130, 20))
        self.label.setObjectName("label")
        self.layoutWidget3 = QtWidgets.QWidget(self.pg_finance)
        self.layoutWidget3.setGeometry(QtCore.QRect(80, 40, 331, 101))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setHorizontalSpacing(40)
        self.formLayout_4.setVerticalSpacing(30)
        self.formLayout_4.setObjectName("formLayout_4")
        self.lb_amount_finance = QtWidgets.QLabel(self.layoutWidget3)
        self.lb_amount_finance.setObjectName("lb_amount_finance")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_amount_finance)
        self.line_fin_amt = QtWidgets.QLineEdit(self.layoutWidget3)
        self.line_fin_amt.setObjectName("line_fin_amt")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_fin_amt)
        self.lb_date_fin = QtWidgets.QLabel(self.layoutWidget3)
        self.lb_date_fin.setObjectName("lb_date_fin")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_date_fin)
        self.finance_date = QtWidgets.QDateTimeEdit(self.layoutWidget3)
        self.finance_date.setReadOnly(False)
        self.finance_date.setObjectName("finance_date")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.finance_date)
        self.layoutWidget4 = QtWidgets.QWidget(self.pg_finance)
        self.layoutWidget4.setGeometry(QtCore.QRect(110, 160, 268, 30))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(80)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_submit_fin = QtWidgets.QPushButton(self.layoutWidget4)
        self.btn_submit_fin.setObjectName("btn_submit_fin")
        self.horizontalLayout_5.addWidget(self.btn_submit_fin)
        self.btn_reset_fin = QtWidgets.QPushButton(self.layoutWidget4)
        self.btn_reset_fin.setObjectName("btn_reset_fin")
        self.horizontalLayout_5.addWidget(self.btn_reset_fin)
        self.stackedWidget.addWidget(self.pg_finance)
        self.pg_repay = QtWidgets.QWidget()
        self.pg_repay.setObjectName("pg_repay")
        self.btn_ok_repay = QtWidgets.QPushButton(self.pg_repay)
        self.btn_ok_repay.setGeometry(QtCore.QRect(200, 210, 89, 25))
        self.btn_ok_repay.setObjectName("btn_ok_repay")
        self.label_3 = QtWidgets.QLabel(self.pg_repay)
        self.label_3.setGeometry(QtCore.QRect(130, 10, 220, 21))
        self.label_3.setObjectName("label_3")
        self.table_repay = QtWidgets.QTableWidget(self.pg_repay)
        self.table_repay.setGeometry(QtCore.QRect(80, 30, 330, 161))
        self.table_repay.setObjectName("table_repay")
        self.table_repay.setColumnCount(0)
        self.table_repay.setRowCount(0)
        self.stackedWidget.addWidget(self.pg_repay)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(20, 10, 461, 30))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_info = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_info.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_info.setObjectName("btn_info")
        self.horizontalLayout.addWidget(self.btn_info)
        self.btn_transfer = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_transfer.setObjectName("btn_transfer")
        self.horizontalLayout.addWidget(self.btn_transfer)
        self.btn_purchase = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_purchase.setObjectName("btn_purchase")
        self.horizontalLayout.addWidget(self.btn_purchase)
        self.btn_finance = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_finance.setObjectName("btn_finance")
        self.horizontalLayout.addWidget(self.btn_finance)
        self.btn_repay = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_repay.setObjectName("btn_repay")
        self.horizontalLayout.addWidget(self.btn_repay)
        self.btn_quit = QtWidgets.QPushButton(self.layoutWidget5)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout.addWidget(self.btn_quit)
        self.layoutWidget6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget6.setGeometry(QtCore.QRect(80, 70, 331, 71))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget6)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.lb_total_b = QtWidgets.QLabel(self.layoutWidget6)
        self.lb_total_b.setObjectName("lb_total_b")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lb_total_b)
        self.line_basic_borr = QtWidgets.QLineEdit(self.layoutWidget6)
        self.line_basic_borr.setReadOnly(True)
        self.line_basic_borr.setObjectName("line_basic_borr")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_basic_borr)
        self.lb_total_l = QtWidgets.QLabel(self.layoutWidget6)
        self.lb_total_l.setObjectName("lb_total_l")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lb_total_l)
        self.line_basic_lent = QtWidgets.QLineEdit(self.layoutWidget6)
        self.line_basic_lent.setReadOnly(True)
        self.line_basic_lent.setObjectName("line_basic_lent")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_basic_lent)
        Companies.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Companies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        Companies.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Companies)
        self.statusbar.setObjectName("statusbar")
        Companies.setStatusBar(self.statusbar)

        self.retranslateUi(Companies)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Companies)

    def retranslateUi(self, Companies):
        _translate = QtCore.QCoreApplication.translate
        Companies.setWindowTitle(_translate("Companies", "MainWindow"))
        self.lb_borrowed.setText(_translate("Companies", "borrowed"))
        self.lb_lent.setText(_translate("Companies", "lent"))
        self.btn_submit_trans.setText(_translate("Companies", "Submit"))
        self.btn_reset_trans.setText(_translate("Companies", "Reset"))
        self.lb_amount_trans.setText(_translate("Companies", "Amount"))
        self.lb_date_trans.setText(_translate("Companies", "Due Date"))
        self.lb_lent_2.setText(_translate("Companies", "lent"))
        self.lb_borrowed_2.setText(_translate("Companies", "borrowed"))
        self.label_2.setText(_translate("Companies", "Purchase"))
        self.lb_from_pur.setText(_translate("Companies", "From"))
        self.lb_amount_pur.setText(_translate("Companies", "Amount"))
        self.lb_date_pur.setText(_translate("Companies", "Due Date"))
        self.btn_submit_pur.setText(_translate("Companies", "Submit"))
        self.btn_reset_pur.setText(_translate("Companies", "Reset"))
        self.label.setText(_translate("Companies", "Finance from bank"))
        self.lb_amount_finance.setText(_translate("Companies", "Amount"))
        self.lb_date_fin.setText(_translate("Companies", "Due date"))
        self.btn_submit_fin.setText(_translate("Companies", "Submit"))
        self.btn_reset_fin.setText(_translate("Companies", "Reset"))
        self.btn_ok_repay.setText(_translate("Companies", "OK"))
        self.label_3.setText(_translate("Companies", "Click on a record to select."))
        self.btn_info.setText(_translate("Companies", "Info"))
        self.btn_transfer.setText(_translate("Companies", "Transfer"))
        self.btn_purchase.setText(_translate("Companies", "Purchase"))
        self.btn_finance.setText(_translate("Companies", "Finance"))
        self.btn_repay.setText(_translate("Companies", "Repay"))
        self.btn_quit.setText(_translate("Companies", "Quit"))
        self.lb_total_b.setText(_translate("Companies", "Total borrowed"))
        self.lb_total_l.setText(_translate("Companies", "Total lent"))
