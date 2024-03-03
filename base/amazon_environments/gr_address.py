from .base import BaseData


class GermanAddress(BaseData):
    def __init__(self):
        super().__init__()
        self.ADDRESS_COUNTRY_OPTIONS.COUNTRY_OPTION = "Almanya"
