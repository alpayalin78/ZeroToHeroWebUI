from datetime import datetime, time

import allure

from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class AmazonMyAccountPage(BasePage):
    AMAZON_MY_ACCOUNT_SECTION = (By.ID, "nav-link-accountList-nav-line-1")
    DROPDOWN_SECTION = (By.XPATH, "//span[@class='a-dropdown-prompt']")
    FULL_NAME = (By.ID, "address-ui-widgets-enterAddressFullName")
    PHONE_NUMBER = (By.ID, "address-ui-widgets-enterAddressPhoneNumber")
    ADDRESS_TEXT = (By.ID, "address-ui-widgets-enterAddressLine1")
    ADDRESS_CITY = (By.ID, "address-ui-widgets-enterAddressCity")
    ADDRESS_STATE_REGION = (By.ID, "address-ui-widgets-enterAddressStateOrRegion")
    ADDRESS_DISTRICT_COUNTY = (By.ID, "address-ui-widgets-enterAddressDistrictOrCounty")
    PLZ_INPUT_GERMAN = (By.ID, "address-ui-widgets-enterAddressPostalCode")
    PLZ_ENTER_ADDRESS_CITY_GERMAN = (By.ID, "address-ui-widgets-enterAddressCity")
    ADD_ADDRESS_BUTTON = (By.XPATH, "//input[@class='a-button-input']")
    AMAZON_ADD_ADDRESS_ICON = (By.ID, "ya-myab-plus-address-icon")

    detail_pages = {
        "Siparişlerim": (By.XPATH, "//h2[contains(text(),'Siparişlerim')]"),
        "Giriş Yapma Ve Güvenlik": (By.XPATH, "//h2[contains(text(),'Giriş Yapma Ve Güvenlik')]"),
        "Prime": (By.XPATH, "//h2[contains(text(),'Prime')]"),
        "Adres": (By.XPATH, "//h2[contains(text(),'Adres')]"),
        "Ödemeleriniz": (By.XPATH, "//h2[contains(text(),'Ödemeleriniz')]"),
        "Hediye Kartları": (By.XPATH, "//h2[contains(text(),'Hediye Kartları')]"),
        "Mesaj Merkezi": (By.XPATH, "//h2[contains(text(),'Mesaj Merkezi')]"),
        "Bize Ulaşın": (By.XPATH, "//h2[contains(text(),'Bize Ulaşın')]"),
        "Listeleriniz": (By.XPATH, "//h2[contains(text(),'Listeleriniz')]"),
        "Amazon Mobil Uygulaması": (By.XPATH, "//h2[contains(text(),'Amazon Mobil Uygulaması')]"),
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """

    @allure.step("navigate_to_details")
    def navigate_to_details(self, account_operation_name="Siparişlerim"):
        """
        Navigate to details in Account Page

        :param account_operation_name: Operation Name
        """
        self.click_element(cursor=self.detail_pages[account_operation_name])
        self.take_screenshot(cursor=self.detail_pages[account_operation_name], color="red")
        self.take_screenshot(cursor=self.AMAZON_ADD_ADDRESS_ICON, color="red")
        self.click_element(cursor=self.AMAZON_ADD_ADDRESS_ICON)

    @allure.step("add_new_address")
    def add_new_address(self,
                        selection: str = "Türkiye",
                        full_name: str = "Alpay",
                        phone_number: str = "5309868574",
                        address_text: str = "Address Text",
                        address_city: str = "İstanbul",
                        address_state_region: str = "Üsküdar",
                        address_district_county: str = "Cumhuriyet Mh."
                        ):
        """
        Adds new address

        :param selection: Selection for Country
        :param full_name: Full name
        :param phone_number: Phone number
        :param address_text: Address Text
        :param address_city: Address City
        :param address_state_region: Address State Region
        :param address_district_county: Address District County
        """
        self.click_element(cursor=self.DROPDOWN_SECTION)
        self.take_screenshot(cursor=self.DROPDOWN_SECTION, color="red")
        self.choose_dropdown(selection=selection, cursor=self.COUNTRIES_SELECTIONS)
        self.take_screenshot(cursor=self.COUNTRIES_SELECTIONS, color="red")
        self.enter_keys(cursor=self.FULL_NAME, text=full_name)
        self.take_screenshot(cursor=self.FULL_NAME, color="red")
        self.enter_keys(cursor=self.PHONE_NUMBER, text=phone_number)
        self.take_screenshot(cursor=self.PHONE_NUMBER, color="red")
        self.enter_keys(cursor=self.ADDRESS_TEXT, text=address_text)
        self.take_screenshot(cursor=self.ADDRESS_TEXT, color="red")
        self.enter_keys(cursor=self.ADDRESS_CITY, text=address_city)
        self.take_screenshot(cursor=self.ADDRESS_CITY, color="red")
        self.enter_keys(cursor=self.ADDRESS_STATE_REGION, text=address_state_region)
        self.take_screenshot(cursor=self.ADDRESS_STATE_REGION, color="red")
        self.enter_keys(cursor=self.ADDRESS_DISTRICT_COUNTY, text=address_district_county)
        self.take_screenshot(cursor=self.ADDRESS_DISTRICT_COUNTY, color="red")
        self.take_screenshot(cursor=self.ADD_ADDRESS_BUTTON, color="red")
        self.click_element(cursor=self.ADD_ADDRESS_BUTTON)
