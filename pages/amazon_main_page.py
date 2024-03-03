import allure

from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AmazonMainPage(BasePage):
    AMAZON_MY_ACCOUNT_SECTION = (By.ID, "nav-link-accountList-nav-line-1")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    MENU_ICON = (By.XPATH, "//i[@class='hm-icon nav-sprite']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """
        self.fluent_wait(30).until(ec.visibility_of_element_located(self.MENU_ICON),
                                   message="Menu Icon is not visible!")
        self.fluent_wait(30).until(ec.visibility_of_element_located(self.SEARCH_BAR),
                                   message="Search Bar is not visible!")
        assert "amazon.com.tr" in self.fetch_current_url(), "URL is not containing login text!"

    @allure.step("navigate_to_my_account_page")
    def navigate_to_my_account_page(self):
        """
        Navigate to My Account Page
        """
        self.take_screenshot(cursor=self.AMAZON_MY_ACCOUNT_SECTION, color="red")
        self.click_element(cursor=self.AMAZON_MY_ACCOUNT_SECTION)

