# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sogis_browser_dock.ui'
#
# Created: Sat Oct 25 17:10:09 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SogisBrowserDock(object):
    def setupUi(self, SogisBrowserDock):
        SogisBrowserDock.setObjectName(_fromUtf8("SogisBrowserDock"))
        SogisBrowserDock.resize(397, 571)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setContentsMargins(0, -1, 0, 0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, 3, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.toolButtonReset = QtGui.QToolButton(self.dockWidgetContents)
        self.toolButtonReset.setObjectName(_fromUtf8("toolButtonReset"))
        self.horizontalLayout.addWidget(self.toolButtonReset)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.treeWidget = QtGui.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget.header().setVisible(False)
        self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 3, -1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dateEdit = QtGui.QDateEdit(self.dockWidgetContents)
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Switzerland))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        SogisBrowserDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(SogisBrowserDock)
        QtCore.QMetaObject.connectSlotsByName(SogisBrowserDock)

    def retranslateUi(self, SogisBrowserDock):
        SogisBrowserDock.setWindowTitle(QtGui.QApplication.translate("SogisBrowserDock", "SO!GIS Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonReset.setText(QtGui.QApplication.translate("SogisBrowserDock", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.dateEdit.setDisplayFormat(QtGui.QApplication.translate("SogisBrowserDock", "dd. MMMM yyyy", None, QtGui.QApplication.UnicodeUTF8))

