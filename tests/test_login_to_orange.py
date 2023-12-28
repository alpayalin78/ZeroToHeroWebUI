from pages import LoginPage


class TestLoginToOrange:
    def test_login_to_orange(self, driver_test, user_information):
        login_page = LoginPage(driver=driver_test)
        login_page.login_to_website(username=user_information.get("username"), password=user_information.get("password"))
