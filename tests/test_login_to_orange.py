import time
from base import BasePage
from pages import LoginPage


class TestLoginToOrange:
    def test_login_to_orange(self, driver_test):
        login_page = LoginPage(driver=driver_test)
        login_page.login_to_website(username="Admin", password="admin123")
        time.sleep(15)
