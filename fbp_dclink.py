from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from common.pydrs import SerialDRS

class FbpDclink(QThread):

    update_gui = pyqtSignal(dict)

    def __init__(self):
        QThread.__init__(self)

        self._is_active = False
        self._baudrate = '6000000'
        #self._baudrate = '115200'
        self._drs = SerialDRS()

        self._screen_readings = {
            'digital_pot_read'  : 0.0,
            'fault_status'      : 0,
            'intlk'             : 0,
            'vdclink_1'         : 0.0,
            'vdclink_2'         : 0.0,
            'vdclink_3'         : 0.0,
            'vdclink_4'         : 0.0
        }

        self._interlocks = [
            'Sobre tensão na fonte 3',
            'Sobre-tensão na fonte 2',
            'Sobre-tensão na fonte 1',
            'Interlock externo',
            'Sensor de fumaça',
            'Falha Fonte 3',
            'Falha Fonte 2',
            'Falha Fonte 1'
        ]

    @property
    def is_active(self):
        return self._is_active

    def connect_serial(self, com_port):
        if com_port is not None:
            res = self._drs.Connect(com_port, self._baudrate)
            self._drs.SetSlaveAdd(20)
        return res

    def disconnect_serial(self):
        res = self._drs.Disconnect()
        return res

    def turn_on(self):
        res = self._drs.turn_on()
        self._is_active = True
        return res

    def turn_off(self):
        res = self._drs.turn_off()
        self._is_active = False
        return res

    def intlk_reset(self):
        self._drs.reset_interlocks()

    def write_reference_voltage(self, val):
        self._drs.set_slowref(val)

    def check_interlocks(self):
        res = True
        intlk = self._drs.read_bsmp_variable(26, 'uint32_t')
        if intlk is 0:
            res = False
        return res

    def get_current_reference(self):
        ref = int(self._drs.read_bsmp_variable(2, 'float'))
        return ref

    def update_params(self):
        try:
            self._screen_readings['vdclink_2']          = round(self._drs.read_bsmp_variable(30, 'float'), 3)
        except:
            pass

        try:
            self._screen_readings['digital_pot_read']   = round(self._drs.read_bsmp_variable(28, 'float'), 3)
        except:
            pass

        try:
            self._screen_readings['intlk']              = self._drs.read_bsmp_variable(26, 'uint32_t')
        except:
            pass

        try:
            self._screen_readings['vdclink_1']          = round(self._drs.read_bsmp_variable(29, 'float'), 3)
        except:
            pass

        try:
            self._screen_readings['vdclink_3']          = round(self._drs.read_bsmp_variable(31, 'float'), 3)
        except:
            pass

        try:
            self._screen_readings['fault_status']       = self._drs.read_bsmp_variable(27, 'uint16_t')
        except:
            pass

        print(self._screen_readings)
        self.update_gui.emit(self._screen_readings)

    def get_intlk_list(self, bitmask):
        bitfield = self._get_bitfield(bitmask)
        mask = bitfield[len(bitfield) - len(self._interlocks):]
        filtered = itertools.compress(self._interlocks, mask)
        return list(filtered)

    def _get_bitfield(self, bitmask):
        bitfield = [int(bit) for bit in bin(bitmask)[2:]] # [2:] to remove '0b'
        return bitfield
