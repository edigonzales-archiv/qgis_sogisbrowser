# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SogisBrowser
                                 A QGIS plugin
 aka SO!GIS Layer laden
                             -------------------
        begin                : 2014-10-25
        copyright            : (C) 2014 by Stefan Ziegler
        email                : edi.gonzales@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SogisBrowser class from file SogisBrowser.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sogis_browser import SogisBrowser
    return SogisBrowser(iface)
