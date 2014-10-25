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

from ui_sogis_browser_dialog import Ui_SogisBrowserDialog

class SogisBrowserDialog(QDialog, Ui_SogisBrowserDialog):
    def __init__(self, parent=None):
        """Constructor."""
        QDialog.__init__(self, parent)
        self.setupUi(self)
