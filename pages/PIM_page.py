from base import BasePage


class PIMPage(BasePage):
    # LOCATORS
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
