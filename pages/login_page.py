from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.fluent_wait(30).until(ec.visibility_of_element_located(self.USERNAME_INPUT),
                                   message="Username Input is not visible!")
        self.fluent_wait(30).until(ec.visibility_of_element_located(self.PASSWORD_INPUT),
                                   message="Password Input is not visible!")
        assert "login" in self.fetch_current_url(), "URL is not containing login text!"

    def login_to_website(self, username: str, password: str):
        """
        Login to the Web Page
        """
        self.driver.find_element(by=self.USERNAME_INPUT[0], value=self.USERNAME_INPUT[1]).send_keys(username)
        self.driver.find_element(by=self.PASSWORD_INPUT[0], value=self.PASSWORD_INPUT[1]).send_keys(password)
        self.driver.find_element(by=self.LOGIN_BUTTON[0], value=self.LOGIN_BUTTON[1]).click()
