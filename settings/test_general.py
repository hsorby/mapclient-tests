'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import unittest

import os, sys

from PySide import QtGui

from mapclient.settings.info import setApplicationsSettings
from mapclient.settings.general import getLogDirectory

test_app = QtGui.QApplication.instance()
if test_app is None:
    test_app = QtGui.QApplication(sys.argv)

setApplicationsSettings(test_app)

class GeneralTestCase(unittest.TestCase):


    def testGetLogLocation(self):
        ll = getLogDirectory()
        self.assertTrue(os.path.exists(ll))
        self.assertTrue(os.access(ll, os.W_OK | os.X_OK))
        
