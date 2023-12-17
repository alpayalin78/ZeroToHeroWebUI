from base import BasePage


class DirectoryPage(BasePage):
    # LOCATORS
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
