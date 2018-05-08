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

    def _enable_fac_acdc_widgets(self):
        self.le_fwr_version_fac_acdc.setEnabled(True)
        self.le_soft_intlk_fac_acdc.setEnabled(True)
        self.pb_soft_intlk_info_fac_acdc.setEnabled(True)
        self.pb_soft_intlk_reset_fac_acdc.setEnabled(True)
        self.le_hard_intlk_fac_acdc.setEnabled(True)
        self.pb_hard_intlk_info_fac_acdc.setEnabled(True)
        self.pb_turn_on_fac_acdc.setEnabled(True)
        self.pb_turn_off_fac_acdc.setEnabled(True)
        self.pb_open_loop_fac_acdc.setEnabled(True)
        self.pb_close_loop_fac_acdc.setEnabled(True)
        self.le_setpoint_fac_acdc.setEnabled(True)
        self.le_reference_fac_acdc.setEnabled(True)
        self.le_slowref_counter_fac_acdc.setEnabled(True)
        self.le_syncpulse_counter_fac_acdc.setEnabled(True)
        self.pb_export_param_fac_acdc.setEnabled(True)
        self.pb_send_param_fac_acdc.setEnabled(True)

    def _disable_fac_acdc_widgets(self):
        self.le_fwr_version_fac_acdc.setEnabled(False)
        self.le_soft_intlk_fac_acdc.setEnabled(False)
        self.pb_soft_intlk_info_fac_acdc.setEnabled(False)
        self.pb_soft_intlk_reset_fac_acdc.setEnabled(False)
        self.le_hard_intlk_fac_acdc.setEnabled(False)
        self.pb_hard_intlk_info_fac_acdc.setEnabled(False)
        self.pb_turn_on_fac_acdc.setEnabled(False)
        self.pb_turn_off_fac_acdc.setEnabled(False)
        self.pb_open_loop_fac_acdc.setEnabled(False)
        self.pb_close_loop_fac_acdc.setEnabled(False)
        self.le_setpoint_fac_acdc.setEnabled(False)
        self.le_reference_fac_acdc.setEnabled(False)
        self.le_slowref_counter_fac_acdc.setEnabled(False)
        self.le_syncpulse_counter_fac_acdc.setEnabled(False)
        self.pb_export_param_fac_acdc.setEnabled(False)
        self.pb_send_param_fac_acdc.setEnabled(False)

    def _enable_fac_dcdc_widgets(self):
        pass

    def _disable_fac_dcdc_widgets(self):
        pass

    def _enable_fap_widgets(self):
        pass

    def _disable_fap_widgets(self):
        pass

    def _enable_fbp_widgets(self):
        pass

    def _disable_fbp_widgets(self):
        pass

    def _enable_dclink_widgets(self):
        pass

    def _disable_dclink_widgets(self):
        pass

    def _connect_signals(self):
        pass


###############################################################################
############################# Run Application #################################
###############################################################################
app = QApplication(sys.argv)
widget = PowerSupplyTestInterface()
widget.show()
sys.exit(app.exec_())
