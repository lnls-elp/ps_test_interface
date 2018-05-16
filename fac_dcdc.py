from common.pydrs import SerialDRS

class FacDcdc:

    def __init__(self):
        self._drs = SerialDRS()
        self._baudrate = '6000000'
        self._is_active = False

        self._screen_readings = {
            'readback'          : 0.0,
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
            'hard_intlk'        : 0
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

    def open_loop(self):
        res = self._drs.open_loop()
        return res

    def close_loop(self):
        res = self._drs.close_loop()
        return res

    def enable_siggen(self):
        pass

    def disable_siggen(self):
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
        res = self._drs.set

    def update_params(self):
        pass
