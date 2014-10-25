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
from qgis.core import *
from qgis.gui import *

import os

from ui_sogis_browser_dock import Ui_SogisBrowserDock

class SogisBrowserDock(QDockWidget, Ui_SogisBrowserDock):
    def __init__(self, parent=None):
        """Constructor."""
        QDockWidget.__init__(self, parent)
        self.setupUi(self)

        self.toolButtonReset.setIcon(QIcon(':/plugins/sogisbrowser/icons/reset.svg'))

        today = QDateTime.currentDateTime()
        self.dateEdit.setDateTime(today)
        self.dateEdit.setCalendarPopup(True)
        
#        self.dateEdit.setLocale(QLocale(QLocale.German));  # Qt Designer
