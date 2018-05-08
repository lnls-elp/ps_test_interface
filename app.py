#!/usr/bin/python3
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import QtGui, uic
import serial
import glob
import sys

class PowerSupplyTestInterface(QWidget):

    def __init__(self, *args):
        super(PowerSupplyTestInterface, self).__init__(*args)
        uic.loadUi('wizard.ui', self)


###############################################################################
############################# Run Application #################################
###############################################################################
app = QApplication(sys.argv)
widget = PowerSupplyTestInterface()
widget.show()
sys.exit(app.exec_())
