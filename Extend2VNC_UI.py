# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Extend2VNC_UI.ui'
#
# Created: Sat Sep 10 17:55:12 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtGui, QtCore, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(629, 197)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.resolution_comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resolution_comboBox.sizePolicy().hasHeightForWidth())
        self.resolution_comboBox.setSizePolicy(sizePolicy)
        self.resolution_comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.resolution_comboBox.setMaximumSize(QtCore.QSize(1600000, 1600000))
        self.resolution_comboBox.setObjectName(_fromUtf8("resolution_comboBox"))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.resolution_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.resolution_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMinimumSize(QtCore.QSize(100, 25))
        self.start_pushButton.setObjectName(_fromUtf8("start_pushButton"))
        self.horizontalLayout.addWidget(self.start_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem4 = QtWidgets.QSpacerItem(85, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.customres_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.customres_lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customres_lineEdit.sizePolicy().hasHeightForWidth())
        self.customres_lineEdit.setSizePolicy(sizePolicy)
        self.customres_lineEdit.setText(_fromUtf8(""))
        self.customres_lineEdit.setObjectName(_fromUtf8("customres_lineEdit"))
        self.horizontalLayout_3.addWidget(self.customres_lineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(278, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.horizontalLayout_2.addWidget(self.status_label)
        spacerItem8 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 629, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionMain_help = QtWidgets.QAction(MainWindow)
        self.actionMain_help.setObjectName(_fromUtf8("actionMain_help"))
        self.actionAbout_Extend2VNC = QtWidgets.QAction(MainWindow)
        self.actionAbout_Extend2VNC.setObjectName(_fromUtf8("actionAbout_Extend2VNC"))
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.menuHelp.addAction(self.actionMain_help)
        self.menuHelp.addAction(self.actionAbout_Extend2VNC)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Extend2VNC", None))
        self.label.setText(_translate("MainWindow", "Resolution", None))
        self.resolution_comboBox.setItemText(0, _translate("MainWindow", "640x480 (VGA)", None))
        self.resolution_comboBox.setItemText(1, _translate("MainWindow", "800x480 (Cell)", None))
        self.resolution_comboBox.setItemText(2, _translate("MainWindow", "1024x600 (Tablet 7\")", None))
        self.resolution_comboBox.setItemText(3, _translate("MainWindow", "1024x768 (Monitor 4:3)", None))
        self.resolution_comboBox.setItemText(4, _translate("MainWindow", "1280x800", None))
        self.resolution_comboBox.setItemText(5, _translate("MainWindow", "1366x768 (Monitor 16:9)", None))
        self.resolution_comboBox.setItemText(6, _translate("MainWindow", "Custom", None))
        self.start_pushButton.setText(_translate("MainWindow", "Start", None))
        self.customres_lineEdit.setPlaceholderText(_translate("MainWindow", "1366x768", None))
        self.status_label.setText(_translate("MainWindow", "Status", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionMain_help.setText(_translate("MainWindow", "Main help", None))
        self.actionAbout_Extend2VNC.setText(_translate("MainWindow", "About Extend2VNC", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))

