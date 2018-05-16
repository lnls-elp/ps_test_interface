from common.pydrs import SerialDRS

class FbpDclink:

    def __init__(self):
        self._is_active = False
        self._baudrate = '6000000'
        self._drs = SerialDRS()
        self._screen_readings = {
            'digital_pot_read'  : 0.0,
            'intlk'             : 0,
            'vdclink_1'         : 0.0,
            'vdclink_2'         : 0.0,
            'vdclink_3'         : 0.0,
            'vdclink_4'         : 0.0
        }

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
        res = self._drs.turn_on()
        return res

    def turn_off(self):
        res = self._drs.turn_off()
        return res

    def intlk_info(self):
        pass

    def intlk_reset(self):
        pass

    def update_params(self):
        pass
