# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SogisBrowserDialog
                                 A QGIS plugin
 aka SO!GIS Layer laden
                             -------------------
        begin                : 2014-10-25
        git sha              : $Format:%H$
        copyright            : (C) 2014 by Stefan Ziegler
        email                : edi.gonzales@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import QNetworkAccessManager
from PyQt4.QtNetwork import QNetworkRequest
from qgis.core import *
from qgis.gui import *

import os
import sys
import json
import collections
import traceback

from ui_sogis_browser_dock import Ui_SogisBrowserDock

class SogisBrowserDock(QDockWidget, Ui_SogisBrowserDock):
    def __init__(self, parent=None):
        """Constructor."""
        QDockWidget.__init__(self, parent)
        self.setupUi(self)
        
        self.SEARCH_URL = "http://www.catais.org/wsgi/search_metadb.wsgi?query="

        self.toolButtonReset.setIcon(QIcon(':/plugins/sogisbrowser/icons/reset.svg'))

        today = QDateTime.currentDateTime()
        self.dateEdit.setDateTime(today)
        self.dateEdit.setCalendarPopup(True)
        
#        self.dateEdit.setLocale(QLocale(QLocale.German));  # Qt Designer

        self.treeWidget.setColumnCount(3)
        self.treeWidget.hideColumn(2)        
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setEditTriggers(QTreeWidget.NoEditTriggers)
        self.treeWidget.setSelectionBehavior(QTreeWidget.SelectRows)
#        self.treeWidget.setFrameStyle(QFrame.Box | QFrame.Plain)
#        self.treeWidget.header().resizeSection(0, 50)
        self.treeWidget.header().setStretchLastSection(False);
        self.treeWidget.header().setResizeMode(0, QHeaderView.Stretch);   
        self.treeWidget.header().setResizeMode(1, QHeaderView.ResizeToContents);   
        
#        self.treeWidget.setDragDropMode( QTreeView.DragDrop )
#        self.treeWidget.setDragEnabled(True) 
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setAcceptDrops(False)

        self.treeWidget.header().hide()
        
        font = QFont()
        font.setPointSize(10)
        self.treeWidget.setFont(font)

        self.networkManager = QNetworkAccessManager(self)
        self.connect(self.networkManager, SIGNAL("finished(QNetworkReply*)"), self.handleNetworkData)

#    def dragEnterEvent(e):
#        e.accept()
#
#    def dragMoveEvent(e):
##      // do not accept drops above/below items
##      /*if ( dropIndicatorPosition() != QAbstractItemView::OnItem )
##      {
##        QgsDebugMsg("drag not on item");
##        e->ignore();
##        return;
##      }*/
#
#        QTreeView.dragMoveEvent( e );
#
#        if not e.mimeData().hasFormat( "application/x-vnd.qgis.qgis.uri" ):
#            e.ignore()
#            return


    def initGui(self):
        request = QNetworkRequest(QUrl(self.SEARCH_URL))
        self.networkManager.get(request)
        
    def handleNetworkData(self, networkReply):    
        url = networkReply.url()
        if not networkReply.error():
            displaytext = []
            category = []
            meta_id = []
            
            response = networkReply.readAll()

            try:
                my_response = unicode(response)
                json_response = json.loads(my_response, object_pairs_hook=collections.OrderedDict) 
            except Exception:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                QMessageBox.critical(None, "SO!GIS Browser", "Failed to load json response" + str(traceback.format_exc(exc_traceback)))                                    
                return
                
            print json_response
            
            for result in json_response['results']:
                displaytext.append(result['displaytext'])
                category.append(result['category'])
                meta_id.append(result['meta_id'])
            
            self.showSearchResult(displaytext, category, meta_id)

    def showSearchResult(self, displaytext, category, meta_id):
        if len(displaytext) == 0:
            return False
            
        pal = self.palette()
        color  = pal.color(QPalette.Disabled, QPalette.WindowText)

        self.treeWidget.setUpdatesEnabled(False)
        self.treeWidget.clear()

        for  i in range(len(displaytext)):
            item = QTreeWidgetItem(self.treeWidget)
            item.setText(0, displaytext[i])
            item.setToolTip(0, displaytext[i])
            
            item.setText(1, category[i])
            item.setTextAlignment(1, Qt.AlignRight)            
            item.setTextColor(1, color)
            
#            item.setText(2, str(meta_id[i]))
#            item.setTextAlignment(2, Qt.AlignRight)
#            item.setTextColor(2, color)
            item.setData(2, Qt.UserRole, meta_id[i])

#        self.treeWidget.setCurrentItem(self.treeWidget.topLevelItem(0))
#        self.treeWidget.resizeColumnToContents(0)
#        self.treeWidget.resizeColumnToContents(1)
        self.treeWidget.adjustSize()
        self.treeWidget.setUpdatesEnabled(True)
