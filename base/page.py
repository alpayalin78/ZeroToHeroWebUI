from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.timeout = 10

    def fluent_wait(self, timeout: float = 10., poll_frequency=0.5, ignored_exceptions=None) -> WebDriverWait:
        """
        Returns WebDriverWait object

        :param timeout: Time amount to be used in waiting
        :param poll_frequency: Frequency rate
        :param ignored_exceptions: Ignore the exceptions except timeout
        :return: WebDriverWait
        """
        return WebDriverWait(driver=self.driver, timeout=timeout,
                             poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)

    def get_current_url(self) -> str:
        """
        Returns current URL

        :return: str
        """
        return self.driver.current_url

    def enter_data(self, locator: WebElement) -> str:
        """
        Returns current URL

        :return: str
        """
        self.driver.sen



        return self.driver.current_url
