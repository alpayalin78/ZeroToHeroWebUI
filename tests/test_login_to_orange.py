import logging


import allure

from pages import LoginPage, MyInfoPage
from base.utils import generate_random_number, generate_random_text


class TestLoginToOrange:
    def test_login_to_orange(self, driver_test, user_information):
        login_page = LoginPage(driver=driver_test)
        login_page.login_to_website(username=user_information.get("username"),
                                    password=user_information.get("password"))

        my_info_page = MyInfoPage(driver=driver_test)

        my_info_page_data = my_info_page.fill_personal_details(first_name=generate_random_text(6),
                                                               middle_name=generate_random_text(6),
                                                               surname_name=generate_random_text(6),
                                                               employee_id=generate_random_number(1),
                                                               driver_license_number=generate_random_number(4),
                                                               ssn_number=generate_random_number(4),
                                                               sin_number=generate_random_number(4),
                                                               nationality="American",
                                                               marital_status="Single",
                                                               gender="Male",
                                                               military_service="Done",
                                                               smoker=True,
                                                               blood_type="A+",
                                                               file_path_to_be_uploaded=r"C:\Users\alpay.alin\Documents\ShareX\Screenshots\2023-12\chrome_0EvFSfkoOR.png",
                                                               comment="Selamlar")

        assert my_info_page_data == "Success"
