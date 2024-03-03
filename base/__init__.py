from base.page import BasePage
from .logger import AllureHandler, configuration, JsonFormatter, detailed_formatter
from base.amazon_environments import BaseData, GermanAddress, TurkeyAddress
from .amazon_constants.address_country_option import AddressCountryOption


class MetaBase:
    pass