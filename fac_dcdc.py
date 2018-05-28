from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from common.pydrs import SerialDRS
import itertools

class FacDcdc(QThread):

    update_gui = pyqtSignal(dict)

    def __init__(self):
        QThread.__init__(self)

        self._drs = SerialDRS()
        self._baudrate = '6000000'
        self._is_active = False
        self._screen_readings = {
            'setpoint'          : 0.0,
            'reference'         : 0.0,
            'slowref_counter'   : 0,
            'syncpulse_counter' : 0,
            'iload_1'           : 0.0,
            'iload_2'           : 0.0,
            'vload'             : 0.0,
            'vcapbank'          : 0.0,
            'induc_temp'        : 0.0,
            'igbt_temp'         : 0.0,
            'duty_cycle'        : 0,
            'soft_intlk'        : 0,
            'hard_intlk'        : 0,
            'fwr_version'       : ''
        }

        self._hard_interlocks = [
            'Falha nos drivers do módulo',
            'Sub-tensão no DCLINK',
            'Sobre-tensão no DCLINK',
            'Sobre-tensão na carga',
            'Sobre-corrente na carga'
        ]

        self._soft_interlocks = [
            'Falha leitura DCCT 2',
            'Falha leitura DCCT 1',
            'Alta diferença entre DCCTs',
            'Falha DCCT 2',
            'Falha DCCT 1',
            'Sobre-temperatura nos indutores',
            'Sobre-temperatura nos indutores'
        ]

    @property
    def is_active(self):
        return self._is_active

    def connect_serial(self, com_port):
        res = False
        if com_port is not None:
            res = self._drs.Connect(com_port, self._baudrate)
            self._is_active = True
        return res

    def disconnect_serial(self):
        res = self._drs.Disconnect()
        self._is_active = False
        return res

    def turn_on(self):
        try:
            self._drs.turn_on()
        except:
            pass

    def turn_off(self):
        try:
            self._drs.turn_off()
        except:
            pass

    def open_loop(self):
        try:
            self._drs.open_loop()
        except:
            pass

    def close_loop(self):
        try:
            self._drs.close_loop()
        except:
            pass

    def enable_siggen(self):
        try:
            self._drs.enable_siggen()
        except:
            pass

    def disable_siggen(self):
        try:
            self._drs.disable_siggen()
        except:
            pass

    def soft_intlk_info(self):
        pass

    def soft_intlk_reset(self):
        pass

    def hard_intlk_info(self):
        pass

    def hard_intlk_reset(self):
        pass

    def send_setpoint(self, value):
        res = self._drs.set_slowref(value)

    def update_params(self):
        try:
            self._screen_readings['setpoint']           = self._drs.read_bsmp_variable(1, 'float')
            self._screen_readings['reference']          = self._drs.read_bsmp_variable(2, 'float')
            self._screen_readings['slowref_counter']    = self._drs.read_bsmp_variable(4, 'uint32_t')
            self._screen_readings['syncpulse_counter']  = self._drs.read_bsmp_variable(5, 'uint32_t')
            self._screen_readings['soft_intlk']         = self._drs.read_bsmp_variable(25, 'uint32_t')
            self._screen_readings['hard_intlk']         = self._drs.read_bsmp_variable(26, 'uint32_t')
            self._screen_readings['iload_1']            = self._drs.read_bsmp_variable(27, 'float')
            self._screen_readings['iload_2']            = self._drs.read_bsmp_variable(28, 'float')
            self._screen_readings['vload']              = self._drs.read_bsmp_variable(29, 'float')
            self._screen_readings['vcapbank']           = self._drs.read_bsmp_variable(30, 'float')
            self._screen_readings['induc_temp']         = self._drs.read_bsmp_variable(31, 'float')
            self._screen_readings['igbt_temp']          = self._drs.read_bsmp_variable(32, 'float')
            self._screen_readings['duty_cycle']         = self._drs.read_bsmp_variable(33, 'float')
            self._screen_readings['fwr_version']        = self._drs.read_udc_arm_version()
            self.update_gui.emit(self._screen_readings)
        except:
            pass

    def get_hard_intlk_list(self, bitmask):
        bitfield = self._get_bitfield(bitmask)
        mask = bitfield[len(bitfield) - len(self._hard_interlocks):]
        filtered = itertools.compress(self._hard_interlocks, mask)
        return list(filtered)

    def get_soft_intlk_list(self, bitmask):
        bitfield = self._get_bitfield(bitmask)
        mask = bitfield[len(bitfield) - len(self._soft_interlocks):]
        filtered = itertools.compress(self._soft_interlocks, mask)
        return list(filtered)

    def _get_bitfield(self, bitmask):
        bitfield = [int(bit) for bit in bin(bitmask)[2:]] # [2:] to remove '0b'
        return bitfield
