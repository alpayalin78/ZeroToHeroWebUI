from .base import BaseData


class TurkeyAddress(BaseData):
    def __init__(self):
        super().__init__()
        self.ADDRESS_COUNTRY_OPTIONS.COUNTRY_OPTION = "Türkiye"
