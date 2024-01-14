from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
import re


class BasePage:
    SIDE_BAR = (By.XPATH, "//a[@class='oxd-main-menu-item']")
    ALERT_POP_UP = (By.XPATH, "(//div[@id='oxd-toaster_1']//p)[1]")

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

    def fetch_current_url(self) -> str:
        """
        Returns current URL

        :return: str
        """
        return self.driver.current_url

    def is_element_clickable(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is clickable

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        try:
            return bool(self.fluent_wait(timeout=timeout).until(ec.element_to_be_clickable(cursor)))

        except TimeoutException:
            return False

    def find_element(self, locator) -> WebElement:
        """
        Find element for the given LOCATOR

        :param locator: Locator
        :return: WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                              message=f"Element <{locator}> is not present")

    def find_elements(self, locator) -> list[WebElement]:
        """
        Find elements for the given LOCATOR

        :param locator: Locator
        :return: list
        """
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))

    def scroll_to_element(self, cursor) -> None:
        """
        Scrolls to the given element on the page

        :param cursor: Locator or Web Element
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.driver.execute_script("arguments[0].scrollIntoView(false)", element)

    def click_element(self, cursor) -> None:
        """
        Clicks to the given element

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_element_clickable(element)
        self.scroll_to_element(element)
        element.click()

    def is_element_displayed(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is displayed

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        if isinstance(cursor, WebElement):
            return cursor.is_displayed()

        try:
            element = self.fluent_wait(timeout=timeout).until(ec.presence_of_element_located(cursor))
            return element.is_displayed()

        except TimeoutException:
            return False

    def click_on_navbar_element(self, locator: tuple) -> None:
        """
        Clicks on navbar element

        :param locator: Collection of the menu element's locator
        """
        navbar_elements = self.find_elements(self.SIDE_BAR)
        navbar_element = list(filter(lambda x: locator[1] == re.sub("[^A-Za-zğüşöçıİĞÜŞÖÇ/\s]",
                                                                    "", x.accessible_name), navbar_elements))[0]
        self.is_element_displayed(navbar_element)
        self.is_element_clickable(navbar_element)
        self.click_element(navbar_element)

    def fetch_element_text(self, cursor) -> str:
        """
        Returns element text

        :param cursor: Locator or Web Element
        :return: str
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        return element.text

    def click_with_javascript_method(self, cursor) -> None:
        """
        Clicks to the given element by javascript method

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_element_clickable(element)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click()", element)

    def enter_keys(self, cursor, text) -> None:
        """
        Enters given text to the input

        :param cursor: Locator or WebElement
        :param text: Given text
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_enabled(element)
        self.scroll_to_element(element)
        element.send_keys(text)

    def clear_keys(self, cursor) -> None:
        """
        Clears the entered input

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_enabled(element)
        self.scroll_to_element(element)
        element.clear()

    def is_element_enabled(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is enabled

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        if isinstance(cursor, WebElement):
            return cursor.is_enabled()

        try:
            element = self.fluent_wait(timeout=timeout).until(ec.presence_of_element_located(cursor))
            return element.is_enabled()

        except TimeoutException:
            return False

    def fetch_alert_message(self) -> str:
        """
        Fetches the alert message
        :return: str
        """
        alert_message = self.fetch_element_text(self.find_element(self.ALERT_POP_UP))

        return alert_message
