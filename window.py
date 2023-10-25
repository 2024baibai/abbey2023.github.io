# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAddCategory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddCategory.setObjectName("pushButtonAddCategory")
        self.horizontalLayout.addWidget(self.pushButtonAddCategory)
        self.pushButtonDelCategory = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelCategory.setObjectName("pushButtonDelCategory")
        self.horizontalLayout.addWidget(self.pushButtonDelCategory)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditNewCategory = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNewCategory.sizePolicy().hasHeightForWidth())
        self.lineEditNewCategory.setSizePolicy(sizePolicy)
        self.lineEditNewCategory.setObjectName("lineEditNewCategory")
        self.gridLayout.addWidget(self.lineEditNewCategory, 0, 1, 1, 1)
        self.comboBoxParentCategory = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxParentCategory.sizePolicy().hasHeightForWidth())
        self.comboBoxParentCategory.setSizePolicy(sizePolicy)
        self.comboBoxParentCategory.setObjectName("comboBoxParentCategory")
        self.gridLayout.addWidget(self.comboBoxParentCategory, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableWidgetCategory = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetCategory.sizePolicy().hasHeightForWidth())
        self.tableWidgetCategory.setSizePolicy(sizePolicy)
        self.tableWidgetCategory.setObjectName("tableWidgetCategory")
        self.tableWidgetCategory.setColumnCount(2)
        self.tableWidgetCategory.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCategory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCategory.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidgetCategory)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAddWebsite = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddWebsite.setObjectName("pushButtonAddWebsite")
        self.horizontalLayout_2.addWidget(self.pushButtonAddWebsite)
        self.pushButtonDelWebsite = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelWebsite.setObjectName("pushButtonDelWebsite")
        self.horizontalLayout_2.addWidget(self.pushButtonDelWebsite)
        self.pushButtonFetch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonFetch.setObjectName("pushButtonFetch")
        self.horizontalLayout_2.addWidget(self.pushButtonFetch)
        self.pushButtonSaveToDB = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSaveToDB.setObjectName("pushButtonSaveToDB")
        self.horizontalLayout_2.addWidget(self.pushButtonSaveToDB)
        self.pushButtonGenerateHTML = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerateHTML.setObjectName("pushButtonGenerateHTML")
        self.horizontalLayout_2.addWidget(self.pushButtonGenerateHTML)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBoxCategory2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCategory2.setObjectName("comboBoxCategory2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBoxCategory2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEditNewName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewName.setObjectName("lineEditNewName")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNewName)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEditNewBio = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewBio.setObjectName("lineEditNewBio")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditNewBio)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEditNewUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewUrl.setObjectName("lineEditNewUrl")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditNewUrl)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEditNewLogo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewLogo.setObjectName("lineEditNewLogo")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditNewLogo)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEditNewRealUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditNewRealUrl.setObjectName("lineEditNewRealUrl")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditNewRealUrl)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.plainTextEditTJScript = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditTJScript.sizePolicy().hasHeightForWidth())
        self.plainTextEditTJScript.setSizePolicy(sizePolicy)
        self.plainTextEditTJScript.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEditTJScript.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEditTJScript.setObjectName("plainTextEditTJScript")
        self.horizontalLayout_5.addWidget(self.plainTextEditTJScript)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.tableWidgetWebsite = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetWebsite.setMinimumSize(QtCore.QSize(600, 300))
        self.tableWidgetWebsite.setObjectName("tableWidgetWebsite")
        self.tableWidgetWebsite.setColumnCount(6)
        self.tableWidgetWebsite.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetWebsite.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidgetWebsite)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TKHacker.net"))
        self.pushButtonAddCategory.setText(_translate("MainWindow", "加分类"))
        self.pushButtonDelCategory.setText(_translate("MainWindow", "删分类"))
        self.label_2.setText(_translate("MainWindow", "父级分类"))
        self.label.setText(_translate("MainWindow", "分类"))
        item = self.tableWidgetCategory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "分类"))
        item = self.tableWidgetCategory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "父级分类"))
        self.pushButtonAddWebsite.setText(_translate("MainWindow", "加网站"))
        self.pushButtonDelWebsite.setText(_translate("MainWindow", "删网站"))
        self.pushButtonFetch.setText(_translate("MainWindow", "一键获取数据"))
        self.pushButtonSaveToDB.setText(_translate("MainWindow", "保存到数据库"))
        self.pushButtonGenerateHTML.setText(_translate("MainWindow", "生成html"))
        self.label_3.setText(_translate("MainWindow", "分类"))
        self.label_4.setText(_translate("MainWindow", "网站名称"))
        self.label_5.setText(_translate("MainWindow", "网站简介"))
        self.label_6.setText(_translate("MainWindow", "网址"))
        self.label_7.setText(_translate("MainWindow", "logo"))
        self.label_9.setText(_translate("MainWindow", "真实跳转"))
        self.label_8.setText(_translate("MainWindow", "统计代码"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "分类"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "网站名称"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "网站简介"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "真实跳转"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "网址"))
        item = self.tableWidgetWebsite.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "logo"))
