import allure

from base.amazon_environments.base import BaseData
from base.amazon_constants.parameter_definitions import ParameterDefinitions
from pages import AmazonLoginPage, AmazonMyAccountPage, AmazonMainPage
from tests import BaseTest
from base import BasePage


class TestLoginToAmazon(BaseTest):
    __doc__ = """{description}"""

    @staticmethod
    def generate_parameters(data: BaseData):
        return {
            "test_login_to_amazon": [{
                "country_option": data.ADDRESS_COUNTRY_OPTIONS.COUNTRY_OPTION,
                "full_name": "alpay",
                "phone_number": "5319823788",
                "address_text": "texttttetet",
                "address_city": "İstanbul",
                "address_state_region": "Üsküdar",
                "address_district_county": "Cumhuriyet Mh.",
            }]}

    @staticmethod
    def description(**kwargs):
        step_list = ["Authenticate with any user",
                     "Login to the Amazon web site"
                     "Navigate to the My account section",
                     "Click to 'Adres' section & then click plus sign",
                     "Fill the form and hit submit button check if address creation has been successful"
                     ]
        parameters_list = (("SHIPMENT QUANTITY", kwargs.get("country_option", ParameterDefinitions.COUNTRY_OPTION) + ' | ' + ParameterDefinitions.COUNTRY_OPTION),
                           ("FULL_NAME", kwargs.get("full_name", ParameterDefinitions.FULL_NAME) + ' | ' + ParameterDefinitions.FULL_NAME),
                           ("PHONE_NUMBER", kwargs.get("phone_number", ParameterDefinitions.PHONE_NUMBER) + ' | ' + ParameterDefinitions.PHONE_NUMBER),
                           ("ADDRESS_TEXT", kwargs.get("address_text", ParameterDefinitions.ADDRESS_TEXT) + ' | ' + ParameterDefinitions.ADDRESS_TEXT),
                           ("ADDRESS_CITY", kwargs.get("address_city", ParameterDefinitions.ADDRESS_CITY) + ' | ' + ParameterDefinitions.ADDRESS_CITY),
                           ("ADDRESS_STATE_REGION", kwargs.get("address_state_region", ParameterDefinitions.ADDRESS_STATE_REGION) + ' | ' + ParameterDefinitions.ADDRESS_STATE_REGION),
                           ("ADDRESS_DISTRICT_COUNT", kwargs.get("address_district_county", ParameterDefinitions.ADDRESS_DISTRICT_COUNT) + ' | ' + ParameterDefinitions.ADDRESS_DISTRICT_COUNT)
                           )
        return BasePage.description_handler(
            test_case_name="Test Login To Amazon",
            test_case_aims="""to test that Login to Amazon website and adjust address details according to the provided parameters""",
            expected_result="""If this case results as passed it means, a new address has been added as expected""",
            step_list=step_list, parameters_list=parameters_list)

    def test_login_to_amazon(self, user_information, country_option, full_name,
                             phone_number,
                             address_text,
                             address_city,
                             address_state_region,
                             address_district_county):
        allure.dynamic.description_html(self.__doc__)

        self.logger.info("Navigate to the Amazon website!")
        login_page = AmazonLoginPage(driver=self.driver)
        self.logger.info("Successfully navigated to the website!")

        self.logger.info("Login to the Amazon account!")
        login_page.login_to_website(username=user_information.get("username"),
                                    password=user_information.get("password"))
        self.logger.info("Successfully logged into the account!")

        self.logger.info("Navigate to the details page!")
        amazon_main_page = AmazonMainPage(driver=self.driver)
        amazon_main_page.navigate_to_my_account_page()
        self.logger.info("Navigated to the details page, successfully!")

        self.logger.info("Navigate to the My Account Page!")
        my_account_page = AmazonMyAccountPage(driver=self.driver)
        my_account_page.navigate_to_details(account_operation_name="Adres")
        self.logger.info("Navigate to the My Account Page!")

        self.logger.info("Add new address with the given parameters!")
        my_account_page.add_new_address(selection=country_option,
                                        full_name=full_name,
                                        phone_number=phone_number,
                                        address_text=address_text,
                                        address_city=address_city,
                                        address_state_region=address_state_region,
                                        address_district_county=address_district_county)
        self.logger.info("Successfully added the new address!")
