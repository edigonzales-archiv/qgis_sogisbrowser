# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sogis_browser_dialog.ui'
#
# Created: Sat Oct 25 15:55:06 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SogisBrowserDialog(object):
    def setupUi(self, SogisBrowserDialog):
        SogisBrowserDialog.setObjectName(_fromUtf8("SogisBrowserDialog"))
        SogisBrowserDialog.resize(400, 300)
        self.button_box = QtGui.QDialogButtonBox(SogisBrowserDialog)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))

        self.retranslateUi(SogisBrowserDialog)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("accepted()")), SogisBrowserDialog.accept)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), SogisBrowserDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SogisBrowserDialog)

    def retranslateUi(self, SogisBrowserDialog):
        SogisBrowserDialog.setWindowTitle(QtGui.QApplication.translate("SogisBrowserDialog", "SO!GIS Browser", None, QtGui.QApplication.UnicodeUTF8))

