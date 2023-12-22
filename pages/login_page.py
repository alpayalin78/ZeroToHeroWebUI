from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON =
    FORGOT_YOUR_PASSWORD_LINK =

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """
        self.fluent_wait(10).until(ec.visibility_of_element_located(self.USERNAME_INPUT),
                                   message="Username Input is not visible!")
        self.fluent_wait(10).until(ec.visibility_of_element_located(self.PASSWORD_INPUT),
                                   message="Password Input is not visible!")
        assert "login" in self.get_current_url(), "URL is not containing login text!"

    def login_to_website(self, username: str, password: str):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.enter_data
        # self.wait_for_element_to_be_visible(locator=self.PASSWORD_INPUT)
