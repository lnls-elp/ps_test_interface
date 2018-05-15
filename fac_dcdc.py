from common.pydrs import SerialDRS

class FacDcdc:

    def __init__(self):
        self._drs = SerialDRS()
        self._baudrate = '6000000'
        self._is_active = False

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

    def update_params(self):
        pass
