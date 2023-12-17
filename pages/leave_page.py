from base import BasePage


class LeavePage(BasePage):
    # LOCATORS
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
