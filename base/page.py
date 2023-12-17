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

    # def wait_for_element_to_be_visible(self, locator, timeout=50):
    #     return WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
