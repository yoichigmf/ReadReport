# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ReadReportDialog
                                 A QGIS plugin
 Read Excel report file
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-11-22
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Yoichi Kayama
        email                : yoichi.kayama@gmail.com
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

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import Qgis
#from qgis.PyQt5.QtWidgets  QSizePolicy

from qgis.gui import QgsMessageBar

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ReadReport_dialog_base.ui'))


class ReadReportDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ReadReportDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        
        #self.bar = QgsMessageBar()
        #self.bar.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Fixed )
        self.setupUi(self)
        #self.verticalLayout_2.addWidget(self.bar)

    def accept(self):
        pass