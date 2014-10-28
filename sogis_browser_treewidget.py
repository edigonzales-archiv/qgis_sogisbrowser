# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class SogisBrowserTreeWidget(QTreeWidget):

    def __init__(self):         
        QTreeWidget.__init__(self, None) 
        self.setColumnCount(3)
        self.hideColumn(2)        
        self.setUniformRowHeights(True)
        self.setRootIsDecorated(False)
        self.setEditTriggers(QTreeWidget.NoEditTriggers)
        self.setSelectionBehavior(QTreeWidget.SelectRows)
        self.setDragEnabled(True)
        self.setAcceptDrops(False)
        
        self.header().setStretchLastSection(False)
        self.header().setResizeMode(0, QHeaderView.Stretch)
        self.header().setResizeMode(1, QHeaderView.ResizeToContents)
        self.header().hide()

