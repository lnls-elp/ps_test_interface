from common.pydrs import SerialDRS

class FbpDclink:

    def __init__(self):
        self._is_active = False

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

    def update_params(self):
        pass
