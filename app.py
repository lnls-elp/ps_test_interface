#!/usr/bin/python3
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import QtGui, uic
from fac_acdc import FacAcdc
from fac_dcdc import FacDcdc
from fbp_dclink import FbpDclink
import serial
import glob
import sys

class PowerSupplyTestInterface(QWidget):

    def __init__(self, *args):
        super(PowerSupplyTestInterface, self).__init__(*args)
        uic.loadUi('wizard.ui', self)

        self._disable_fac_dcdc_widgets()
        self._disable_fac_acdc_widgets()

        self._update_time = -1

        self._fac_acdc      = FacAcdc()
        self._fac_dcdc      = FacDcdc()
        self._fbp_dclink    = FbpDclink()

        self.pb_serial_disconnect_fac_dcdc.setEnabled(False)
        self.pb_serial_disconnect_fac_acdc.setEnabled(False)

        self._list_serial_ports()
        self._connect_signals()

###############################################################################
########################### GUI Initialization ################################
###############################################################################
    def _enable_fac_acdc_widgets(self):
        self.le_fwr_version_fac_acdc.setEnabled(True)
        self.le_soft_intlk_fac_acdc.setEnabled(True)
        self.pb_soft_intlk_info_fac_acdc.setEnabled(True)
        self.pb_soft_intlk_reset_fac_acdc.setEnabled(True)
        self.pb_hard_intlk_info_fac_acdc.setEnabled(True)
        self.pb_hard_intlk_reset_fac_acdc.setEnabled(True)
        self.le_hard_intlk_fac_acdc.setEnabled(True)
        self.pb_hard_intlk_info_fac_acdc.setEnabled(True)
        self.pb_turn_on_fac_acdc.setEnabled(True)
        self.pb_turn_off_fac_acdc.setEnabled(True)
        self.pb_open_loop_fac_acdc.setEnabled(True)
        self.pb_close_loop_fac_acdc.setEnabled(True)
        self.le_setpoint_fac_acdc.setEnabled(True)
        self.le_readback_fac_acdc.setEnabled(True)
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
        self.le_soft_intlk_fac_acdc.setEnabled(False)
        self.pb_hard_intlk_info_fac_acdc.setEnabled(False)
        self.pb_hard_intlk_reset_fac_acdc.setEnabled(False)
        self.le_hard_intlk_fac_acdc.setEnabled(False)
        self.pb_turn_on_fac_acdc.setEnabled(False)
        self.pb_turn_off_fac_acdc.setEnabled(False)
        self.pb_open_loop_fac_acdc.setEnabled(False)
        self.pb_close_loop_fac_acdc.setEnabled(False)
        self.le_setpoint_fac_acdc.setEnabled(False)
        self.le_readback_fac_acdc.setEnabled(False)
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
        self.le_readback_fac_dcdc.setEnabled(True)
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
        self.le_readback_fac_dcdc.setEnabled(False)
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

    def _enable_fbp_dclink_widgets(self):
        self.sl_digital_pot_fbp_dclink.setEnabled(True)
        self.le_digital_pot_write_fbp_dclink.setEnabled(True)
        self.pb_turn_on_fbp_dclink.setEnabled(True)
        self.pb_turn_off_fbp_dclink.setEnabled(True)
        self.pb_intlk_info_fbp_dclink.setEnabled(True)
        self.pb_intlk_reset_fbp_dclink.setEnabled(True)
        self.le_intlk_fbp_dclink.setEnabled(True)
        self.le_vdclink_1_fbp_dclink.setEnabled(True)
        self.le_vdclink_2_fbp_dclink.setEnabled(True)
        self.le_vdclink_3_fbp_dclink.setEnabled(True)
        self.le_vdclink_4_fbp_dclink.setEnabled(True)

    def _disable_fbp_dclink_widgets(self):
        self.sl_digital_pot_fbp_dclink.setEnabled(False)
        self.le_digital_pot_write_fbp_dclink.setEnabled(False)
        self.pb_turn_on_fbp_dclink.setEnabled(False)
        self.pb_turn_off_fbp_dclink.setEnabled(False)
        self.pb_intlk_info_fbp_dclink.setEnabled(False)
        self.pb_intlk_reset_fbp_dclink.setEnabled(False)
        self.le_intlk_fbp_dclink.setEnabled(False)
        self.le_vdclink_1_fbp_dclink.setEnabled(False)
        self.le_vdclink_2_fbp_dclink.setEnabled(False)
        self.le_vdclink_3_fbp_dclink.setEnabled(False)
        self.le_vdclink_4_fbp_dclink.setEnabled(False)

    def _connect_signals(self):
        #General
        self.pb_force_params_update.clicked.connect(self._force_update_params)

        # FAC DCDC
        self.pb_serial_connect_fac_dcdc.clicked.connect(self._connect_serial_fac_dcdc)
        self.pb_serial_disconnect_fac_dcdc.clicked.connect(self._disconnect_serial_fac_dcdc)
        self.pb_turn_on_fac_dcdc.clicked.connect(self._turn_on_fac_dcdc)
        self.pb_turn_off_fac_dcdc.clicked.connect(self._turn_off_fac_dcdc)
        self.pb_open_loop_fac_dcdc.clicked.connect(self._open_loop_fac_dcdc)
        self.pb_close_loop_fac_dcdc.clicked.connect(self._close_loop_fac_dcdc)
        self.pb_siggen_enable_fac_dcdc.clicked.connect(self._siggen_enable_fac_dcdc)
        self.pb_siggen_disable_fac_dcdc.clicked.connect(self._siggen_disable_fac_dcdc)
        self.pb_soft_intlk_info_fac_dcdc.clicked.connect(self._soft_intlk_info_fac_dcdc)
        self.pb_soft_intlk_reset_fac_dcdc.clicked.connect(self._soft_intlk_reset_fac_dcdc)
        self.pb_hard_intlk_info_fac_dcdc.clicked.connect(self._hard_intlk_reset_fac_dcdc)
        self.pb_hard_intlk_reset_fac_dcdc.clicked.connect(self._hard_intlk_reset_fac_dcdc)
        self.pb_export_param_fac_dcdc.clicked.connect(self._export_params_fac_dcdc)
        self.pb_send_param_fac_dcdc.clicked.connect(self._send_params_fac_dcdc)
        self._fac_dcdc.update_gui.connect(self._update_gui_fac_dcdc)

        # FAC ACDC
        self.pb_serial_connect_fac_acdc.clicked.connect(self._connect_serial_fac_acdc)
        self.pb_serial_disconnect_fac_acdc.clicked.connect(self._disconnect_serial_fac_acdc)
        self.pb_turn_on_fac_acdc.clicked.connect(self._turn_on_fac_acdc)
        self.pb_turn_off_fac_acdc.clicked.connect(self._turn_off_fac_acdc)
        self.pb_open_loop_fac_acdc.clicked.connect(self._open_loop_fac_acdc)
        self.pb_close_loop_fac_acdc.clicked.connect(self._close_loop_fac_acdc)
        self.pb_export_param_fac_acdc.clicked.connect(self._export_params_fac_acdc)
        self.pb_send_param_fac_acdc.clicked.connect(self._send_params_fac_acdc)

        # FBP DCLINK
        self.pb_serial_connect_fbp_dclink.clicked.connect(self._connect_serial_fbp_dclink)
        self.pb_serial_disconnect_fbp_dclink.clicked.connect(self._disconnect_serial_fbp_dclink)
        self.pb_turn_on_fbp_dclink.clicked.connect(self._turn_on_fbp_dclink)
        self.pb_turn_off_fbp_dclink.clicked.connect(self._turn_off_fbp_dclink)
        self.pb_intlk_info_fbp_dclink.clicked.connect(self._intlk_info_fbp_dclink)
        self.pb_intlk_reset_fbp_dclink.clicked.connect(self._intlk_reset_fbp_dclink)

###############################################################################
################################ GUI Update ###################################
###############################################################################
    def _update_gui_params(self):

        if self._fac_dcdc.is_active:
            self._fac_dcdc.update_params()
        elif self._fac_acdc.is_active:
            self._fac_acdc.update_params()
        elif self._fbp_dclink.is_active:
            self._fbp_dclink.update_params()

    @pyqtSlot(dict)
    def _update_gui_fac_dcdc(self, params):
        self.le_readback_fac_dcdc.setText(str(params['reference']))
        self.le_slowref_counter_fac_dcdc.setText(str(params['slowref_counter']))
        self.le_syncpulse_counter_fac_dcdc.setText(str(params['syncpulse_counter']))
        self.le_soft_intlk_fac_dcdc.setText(str(params['soft_intlk']))
        self.le_hard_intlk_fac_dcdc.setText(str(params['hard_intlk']))
        self.le_iload_1_fac_dcdc.setText(str(params['iload_1']))
        self.le_iload_2_fac_dcdc.setText(str(params['iload_2']))
        self.le_vload_fac_dcdc.setText(str(params['vload']))
        self.le_vcapbank_fac_dcdc.setText(str(params['vcapbank']))
        self.le_induc_temp_fac_dcdc.setText(str(params['induc_temp']))
        self.le_igbt_temp_fac_dcdc.setText(str(params['igbt_temp']))
        self.le_duty_cycle_fac_dcdc.setText(str(params['duty_cycle']))
        self.le_fwr_version_fac_dcdc.setText(params['fwr_version'])

    @pyqtSlot(dict)
    def _update_gui_fac_acdc(self, params):
        pass

    @pyqtSlot(dict)
    def _update_gui_fbp_dclink(self, params):
        self.le_digital_pot_write_fbp_dclink.setText(str(params['digital_pot_read']))
        self.le_intlk_fbp_dclink.setText(str(params['intlk']))
        self.le_vdclink_1_fbp_dclink.setText(str(params['vdclink_1']))
        self.le_vdclink_2_fbp_dclink.setText(str(params['vdclink_2']))
        self.le_vdclink_3_fbp_dclink.setText(str(params['vdclink_3']))
        self.le_vdclink_4_fbp_dclink.setText(str(params['vdclink_4']))

###############################################################################
############################# System Methods ##################################
###############################################################################
    def _list_serial_ports(self):
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsuported platform')

        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.cb_comport_fac_dcdc.addItem(port)
                self.cb_comport_fac_acdc.addItem(port)
                self.cb_comport_fbp_dclink.addItem(port)
            except (OSError, serial.SerialException):
                pass

    def _force_update_params(self):
        self._update_gui_params()

###############################################################################
############################ FAC DCDC Slots ###################################
###############################################################################

    @pyqtSlot()
    def _connect_serial_fac_dcdc(self):
        try:
            port = str(self.cb_comport_fac_dcdc.currentText())
            res = self._fac_dcdc.connect_serial(port)
            if res:
                self.pb_serial_connect_fac_dcdc.setEnabled(False)
                self.cb_comport_fac_dcdc.setEnabled(False)
                self.pb_serial_disconnect_fac_dcdc.setEnabled(True)
                self._enable_fac_dcdc_widgets()
                self.pb_turn_off_fac_dcdc.setEnabled(False)
                self.pb_open_loop_fac_dcdc.setEnabled(False)
                self.pb_siggen_disable_fac_dcdc.setEnabled(False)

                self._update_gui_params()
        except:
            pass

    @pyqtSlot()
    def _disconnect_serial_fac_dcdc(self):
        try:
            res = self._fac_dcdc.disconnect_serial()
            if res:
                self.pb_serial_connect_fac_dcdc.setEnabled(True)
                self.cb_comport_fac_dcdc.setEnabled(True)
                self.pb_serial_disconnect_fac_dcdc.setEnabled(False)
                self._disable_fac_dcdc_widgets()
        except:
            pass

    @pyqtSlot()
    def _turn_on_fac_dcdc(self):
        self._fac_dcdc.turn_on()
        self.pb_turn_on_fac_dcdc.setEnabled(False)
        self.pb_turn_off_fac_dcdc.setEnabled(True)
        self._update_gui_params()

    @pyqtSlot()
    def _turn_off_fac_dcdc(self):
        self._fac_dcdc.turn_off()
        self.pb_turn_on_fac_dcdc.setEnabled(True)
        self.pb_turn_off_fac_dcdc.setEnabled(False)
        self._update_gui_params()

    @pyqtSlot()
    def _open_loop_fac_dcdc(self):
        self._fac_dcdc.open_loop()
        self.pb_open_loop_fac_dcdc.setEnabled(False)
        self.pb_close_loop_fac_dcdc.setEnabled(True)

    @pyqtSlot()
    def _close_loop_fac_dcdc(self):
        self._fac_dcdc.close_loop()
        self.pb_open_loop_fac_dcdc.setEnabled(True)
        self.pb_close_loop_fac_dcdc.setEnabled(False)

    @pyqtSlot()
    def _siggen_enable_fac_dcdc(self):
        res = self._fac_dcdc.enable_siggen()
        if res:
            self.pb_siggen_enable_fac_dcdc.setEnabled(False)
            self.pb_siggen_disable_fac_dcdc.setEnabled(True)

    @pyqtSlot()
    def _siggen_disable_fac_dcdc(self):
        res = self._fac_dcdc.disable_siggen()
        if res:
            self.pb_siggen_enable_fac_dcdc.setEnabled(True)
            self.pb_siggen_disable_fac_dcdc.setEnabled(False)

    @pyqtSlot()
    def _soft_intlk_info_fac_dcdc(self):
        res = self._fac_dcdc.soft_intlk_info()

    @pyqtSlot()
    def _soft_intlk_reset_fac_dcdc(self):
        res = self._fac_dcdc.soft_intlk_reset()

    @pyqtSlot()
    def _hard_intlk_info_fac_dcdc(self):
        res = self._fac_dcdc.hard_intlk_info()

    @pyqtSlot()
    def _hard_intlk_reset_fac_dcdc(self):
        res = self._fac_dcdc.hard_intlk_reset()

    @pyqtSlot()
    def _export_params_fac_dcdc(self):
        pass

    @pyqtSlot()
    def _send_params_fac_dcdc(self):
        pass

###############################################################################
############################ FAC ACDC Slots ###################################
###############################################################################

    @pyqtSlot()
    def _connect_serial_fac_acdc(self):
        try:
            port = str(self.cb_comport_fac_acdc.currentText())
            res = self._fac_acdc.connect_serial(port)
            if res:
                self.pb_serial_connect_fac_acdc.setEnabled(False)
                self.cb_comport_fac_acdc.setEnabled(False)
                self.pb_serial_disconnect_fac_acdc.setEnabled(True)
                self._enable_fac_acdc_widgets()
                self.pb_turn_off_fac_acdc.setEnabled(False)
                self.pb_open_loop_fac_acdc.setEnabled(False)
                self.pb_siggen_disable_fac_acdc.setEnabled(False)
        except:
            pass

    @pyqtSlot()
    def _disconnect_serial_fac_acdc(self):
        try:
            res = self._fac_acdc.disconnect_serial()
            if res:
                self.pb_serial_connect_fac_acdc.setEnabled(True)
                self.cb_comport_fac_acdc.setEnabled(True)
                self.pb_serial_disconnect_fac_acdc.setEnabled(False)
                self._disable_fac_acdc_widgets()
        except:
            pass

    @pyqtSlot()
    def _turn_on_fac_acdc(self):
        res = self._fac_acdc.turn_on()
        if res:
            self.pb_turn_on_fac_acdc.setEnabled(False)
            self.pb_turn_off_fac_acdc.setEnabled(True)

    @pyqtSlot()
    def _turn_off_fac_acdc(self):
        res = self._fac_acdc.turn_off()
        if res:
            self.pb_turn_on_fac_acdc.setEnabled(True)
            self.pb_turn_off_fac_acdc.setEnabled(False)

    @pyqtSlot()
    def _open_loop_fac_acdc(self):
        res = self._fac_acdc.open_loop()
        if res:
            self.pb_open_loop_fac_acdc.setEnabled(False)
            self.pb_close_loop_fac_acdc.setEnabled(True)

    @pyqtSlot()
    def _close_loop_fac_acdc(self):
        res = self._fac_acdc.close_loop()
        if res:
            self.pb_open_loop_fac_acdc.setEnabled(True)
            self.pb_close_loop_fac_acdc.setEnabled(False)

    @pyqtSlot()
    def _export_params_fac_acdc(self):
        pass

    @pyqtSlot()
    def _send_params_fac_acdc(self):
        pass

###############################################################################
############################ FBP DCLINK Slots #################################
###############################################################################

    @pyqtSlot()
    def _connect_serial_fbp_dclink(self):
        try:
            port = str(self.cb_comport_fbp_dclink.currentText())
            res = self._fbp_dclink.connect_serial(port)
            if res:
                self.pb_serial_connect_fbp_dclink.setEnabled(False)
                self.cb_comport_fbp_dclink.setEnabled(False)
                self.pb_serial_disconnect_fbp_dclink.setEnabled(True)
                self._enable_fbp_dclink_widgets()
                self.pb_turn_off_fbp_dclink.setEnabled(False)
        except:
            pass

    @pyqtSlot()
    def _disconnect_serial_fbp_dclink(self):
        try:
            res = self._fbp_dclink.disconnect_serial()
            if res:
                self.pb_serial_connect_fbp_dclink.setEnabled(True)
                self.cb_comport_fbp_dclink.setEnabled(True)
                self.pb_serial_disconnect_fbp_dclink.setEnabled(False)
                self._disable_fbp_dclink_widgets()
        except:
            pass

    @pyqtSlot()
    def _turn_on_fbp_dclink(self):
        res = self._fbp_dclink.turn_on()
        if res:
            self.pb_turn_on_fbp_dclink.setEnabled(False)
            self.pb_turn_off_fbp_dclink.setEnabled(True)

    @pyqtSlot()
    def _turn_off_fbp_dclink(self):
        res = self._fbp_dclink.turn_off()
        if res:
            self.pb_turn_on_fbp_dclink.setEnabled(True)
            self.pb_turn_off_fbp_dclink.setEnabled(False)

    @pyqtSlot()
    def _intlk_info_fbp_dclink(self):
        pass

    @pyqtSlot()
    def _intlk_reset_fbp_dclink(self):
        pass

    @pyqtSlot()
    def send_setpoint_fac_dcdc(self):
        sp = le_setpoint_fac_dcdc.text()
        if sp is not None:
            value = float(sp)
            self._fac_dcdc.send_setpoint(value)

###############################################################################
############################# Run Application #################################
###############################################################################
app = QApplication(sys.argv)
widget = PowerSupplyTestInterface()
widget.show()
sys.exit(app.exec_())
