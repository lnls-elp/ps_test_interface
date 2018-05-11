from common.pydrs import SerialDRS

class FbpDclink:

    def __init__(self):
        self._is_active = False

    @property
    def is_active(self):
        return self._is_active
