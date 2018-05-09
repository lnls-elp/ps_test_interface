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
        self.le_vcapbank_fac_acdc.setEnabled(True)
        self.le_vret_out_fac_acdc.setEnabled(True)
        self.le_iret_out_fac_acdc.setEnabled(True)
        self.le_heatsink_temp_fac_acdc.setEnabled(True)
        self.le_induc_temp_fac_acdc.setEnabled(True)
        self.le_duty_cycle_fac_acdc.setEnabled(True)

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
        self.le_vcapbank_fac_acdc.setEnabled(False)
        self.le_vret_out_fac_acdc.setEnabled(False)
        self.le_iret_out_fac_acdc.setEnabled(False)
        self.le_heatsink_temp_fac_acdc.setEnabled(False)
        self.le_induc_temp_fac_acdc.setEnabled(False)
        self.le_duty_cycle_fac_acdc.setEnabled(False)

    def _enable_fac_dcdc_widgets(self):
        self.pb_turn_on_fac_dcdc.setEnabled(True)
        self.pb_turn_off_fac_dcdc.setEnabled(True)
        self.pb_open_loop_fac_dcdc.setEnabled(True)
        self.pb_close_loop_fac_dcdc.setEnabled(True)
        self.le_setpoint_fac_dcdc.setEnabled(True)
        self.le_reference_fac_dcdc.setEnabled(True)
        self.le_soft_intlk_fac_dcdc.setEnabled(True)
        self.pb_soft_intlk_info_fac_dcdc.setEnabled(True)
        self.pb_soft_intlk_reset_fac_dcdc.setEnabled(True)
        self.le_slowref_counter_fac_dcdc.setEnabled(True)
        self.le_syncpulse_counter_fac_dcdc.setEnabled(True)
        self.le_hard_intlk_fac_dcdc.setEnabled(True)
        self.pb_hard_intlk_info_fac_dcdc.setEnabled(True)
        self.cb_signal_fac_dcdc.setEnabled(True)
        self.pb_hard_intlk_reset_fac_dcdc.setEnabled(True)
        self.le_cyc_counter_fac_dcdc.setEnabled(True)
        self.le_frequence_fac_acdc.setEnabled(True)
        self.le_iter_index_fac_dcdc.setEnabled(True)
        self.le_amplitude_fac_dcdc.setEnabled(True)
        self.le_offset_fac_dcdc.setEnabled(True)
        self.le_siggen_aux_1_fac_dcdc.setEnabled(True)
        self.le_siggen_aux_2_fac_dcdc.setEnabled(True)
        self.le_siggen_aux_3_fac_dcdc.setEnabled(True)
        self.le_siggen_aux_4_fac_dcdc.setEnabled(True)
        self.pb_siggen_enable_fac_dcdc.setEnabled(True)
        self.pb_siggen_disable_fac_dcdc.setEnabled(True)
        self.le_iload_1_fac_dcdc.setEnabled(True)
        self.le_iload_2_fac_dcdc.setEnabled(True)
        self.le_vload_fac_dcdc.setEnabled(True)
        self.le_vcapbank_fac_dcdc.setEnabled(True)
        self.le_induc_temp_fac_dcdc.setEnabled(True)
        self.le_igbt_temp_fac_dcdc.setEnabled(True)
        self.le_duty_cycle_fac_dcdc.setEnabled(True)
        self.le_fwr_version_fac_dcdc.setEnabled(True)
        self.pb_export_param_fac_dcdc.setEnabled(True)
        self.pb_send_param_fac_dcdc.setEnabled(True)

    def _disable_fac_dcdc_widgets(self):
        self.pb_turn_on_fac_dcdc.setEnabled(False)
        self.pb_turn_off_fac_dcdc.setEnabled(False)
        self.pb_open_loop_fac_dcdc.setEnabled(False)
        self.pb_close_loop_fac_dcdc.setEnabled(False)
        self.le_setpoint_fac_dcdc.setEnabled(False)
        self.le_reference_fac_dcdc.setEnabled(False)
        self.le_soft_intlk_fac_dcdc.setEnabled(False)
        self.pb_soft_intlk_info_fac_dcdc.setEnabled(False)
        self.pb_soft_intlk_reset_fac_dcdc.setEnabled(False)
        self.le_slowref_counter_fac_dcdc.setEnabled(False)
        self.le_syncpulse_counter_fac_dcdc.setEnabled(False)
        self.le_hard_intlk_fac_dcdc.setEnabled(False)
        self.pb_hard_intlk_info_fac_dcdc.setEnabled(False)
        self.cb_signal_fac_dcdc.setEnabled(False)
        self.pb_hard_intlk_reset_fac_dcdc.setEnabled(False)
        self.le_cyc_counter_fac_dcdc.setEnabled(False)
        self.le_frequence_fac_acdc.setEnabled(False)
        self.le_iter_index_fac_dcdc.setEnabled(False)
        self.le_amplitude_fac_dcdc.setEnabled(False)
        self.le_offset_fac_dcdc.setEnabled(False)
        self.le_siggen_aux_1_fac_dcdc.setEnabled(False)
        self.le_siggen_aux_2_fac_dcdc.setEnabled(False)
        self.le_siggen_aux_3_fac_dcdc.setEnabled(False)
        self.le_siggen_aux_4_fac_dcdc.setEnabled(False)
        self.pb_siggen_enable_fac_dcdc.setEnabled(False)
        self.pb_siggen_disable_fac_dcdc.setEnabled(False)
        self.le_iload_1_fac_dcdc.setEnabled(False)
        self.le_iload_2_fac_dcdc.setEnabled(False)
        self.le_vload_fac_dcdc.setEnabled(False)
        self.le_vcapbank_fac_dcdc.setEnabled(False)
        self.le_induc_temp_fac_dcdc.setEnabled(False)
        self.le_igbt_temp_fac_dcdc.setEnabled(False)
        self.le_duty_cycle_fac_dcdc.setEnabled(False)
        self.le_fwr_version_fac_dcdc.setEnabled(False)
        self.pb_export_param_fac_dcdc.setEnabled(False)
        self.pb_send_param_fac_dcdc.setEnabled(False)

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
############################### PyQT Slots ####################################
###############################################################################

    @pyqtSlot()
    def _connect_serial_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _disconnect_serial_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _turn_on_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _turn_off_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _open_loop_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _close_loop_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _siggen_enable_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _siggen_disable_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _soft_intlk_info_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _soft_intlk_reset_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _hard_intlk_info_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _hard_intlk_reset_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _export_params_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _send_params_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _connect_serial_fac_acdc(self):
        pass

    @pyqtSlot()
    def _disconnect_serial_fac_acdc(self):
        pass

    @pyqtSlot()
    def _turn_on_fac_acdc(self):
        pass

    @pyqtSlot()
    def _turn_off_fac_acdc(self):
        pass

    @pyqtSlot()
    def _open_loop_fac_acdc(self):
        pass

    @pyqtSlot()
    def _close_loop_fac_acdc(self):
        pass

###############################################################################
############################# Run Application #################################
###############################################################################
app = QApplication(sys.argv)
widget = PowerSupplyTestInterface()
widget.show()
sys.exit(app.exec_())
