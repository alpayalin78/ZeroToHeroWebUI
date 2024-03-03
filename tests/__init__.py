from logging import Logger
from selenium.webdriver import Chrome
import pytest


@pytest.mark.usefixtures("initialize_web_ui")
class BaseTest:
    logger: Logger
    driver: Chrome
