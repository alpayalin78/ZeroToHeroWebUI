from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AmazonLoginPage(BasePage):
    AMAZON_LOGIN_SECTION = (By.ID, "nav-link-accountList-nav-line-1")
    AMAZON_EMAIL_INPUT = (By.ID, "ap_email")
    AMAZON_PASSWORD_INPUT = (By.ID, "ap_password")
    AMAZON_CONTINUE_BUTTON = (By.ID, "continue")
    AMAZON_SIGN_IN_BUTTON = (By.ID, "signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """
        self.driver.get("https://www.amazon.com.tr/")
        self.fluent_wait(30).until(ec.visibility_of_element_located(self.AMAZON_LOGIN_SECTION),
                                   message="Login Section is not visible!")
        assert "amazon.com.tr" in self.fetch_current_url(), "URL is not containing login text!"

    def login_to_website(self, username: str, password: str):
        """
        Login to the Web Page

        :param username: Username
        :param password: Password
        """
        self.take_screenshot(cursor=self.AMAZON_LOGIN_SECTION, color="red")
        self.click_element(cursor=self.AMAZON_LOGIN_SECTION)
        self.enter_keys(cursor=self.AMAZON_EMAIL_INPUT, text=username)
        self.take_screenshot(cursor=self.AMAZON_EMAIL_INPUT, color="red")
        self.take_screenshot(cursor=self.AMAZON_CONTINUE_BUTTON, color="red")
        self.click_element(cursor=self.AMAZON_CONTINUE_BUTTON)
        self.enter_keys(cursor=self.AMAZON_PASSWORD_INPUT, text=password)
        self.take_screenshot(cursor=self.AMAZON_PASSWORD_INPUT, color="red")
        self.take_screenshot(cursor=self.AMAZON_SIGN_IN_BUTTON, color="red")
        self.click_element(cursor=self.AMAZON_SIGN_IN_BUTTON)
