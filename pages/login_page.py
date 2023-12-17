from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_to_website(self, username: str, password: str):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # self.wait_for_element_to_be_visible(locator=self.PASSWORD_INPUT)
