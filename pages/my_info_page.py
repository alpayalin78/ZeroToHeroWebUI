import time

from base import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class MyInfoPage(BasePage):
    LOGO = (By.XPATH, "//a[@class='oxd-brand']")
    PERSONAL_DETAILS_TAB = (By.XPATH, "//a[contains(text(),'Personal Details')]")
    CONTACT_DETAILS_TAB = (By.XPATH, "//a[contains(text(),'Contact Details')]")
    EMERGENCY_CONTACTS_TAB = (By.XPATH, "//a[contains(text(),'Emergency Contacts')]")
    DEPENDENTS_TAB = (By.XPATH, "//a[contains(text(),'Dependents')]")
    IMMIGRATION_TAB = (By.XPATH, "//a[contains(text(),'Immigration')]")
    JOB_TAB = (By.XPATH, "//a[contains(text(),'Job')]")
    SALARY_TAB = (By.XPATH, "//a[contains(text(),'Salary')]")
    TAX_EXEMPTIONS_TAB = (By.XPATH, "//a[contains(text(),'Tax Exemptions')]")
    REPORT_TO_TAB = (By.XPATH, "//a[contains(text(),'Report-to')]")
    QUALIFICATIONS_TAB = (By.XPATH, "//a[contains(text(),'Qualifications')]")
    MEMBERSHIPS_TAB = (By.XPATH, "//a[contains(text(),'Memberships')]")
    LEFT_NAVBAR_MY_INFO_PAGE = (By.LINK_TEXT, "My Info")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='firstName']")
    MIDDLE_NAME_INPUT = (By.XPATH, "//input[@name='middleName']")
    SURNAME_INPUT = (By.XPATH, "//input[@name='lastName']")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input")
    DRIVER_LICENSE_NUMBER_INPUT = (
        By.XPATH, "//label[contains(text(),'License Number')]/parent::div/following-sibling::div/input")
    LICENSE_EXPIRY_DATE = (By.XPATH, "(//div[@class='oxd-date-input']/input)[1]")
    LICENSE_EXPIRY_DATE_CALENDAR_WRAPPER_DATES = (
    By.XPATH, "//div[@class='oxd-calendar-wrapper']//div[@class='oxd-calendar-date-wrapper']")
    SSN_NUMBER_INPUT = (By.XPATH, "//label[contains(text(),'SSN Number')]/parent::div/following-sibling::div/input")
    SIN_NUMBER_INPUT = (By.XPATH, "//label[contains(text(),'SIN Number')]/parent::div/following-sibling::div/input")
    NATIONALITY_DROPDOWN = (By.XPATH, "//div[@class='oxd-select-text-input']")
    MARITAL_STATUS_DROPDOWN = (
        By.XPATH, "(//div[@class='oxd-select-wrapper'])[2]/div/div")
    MARITAL_STATUS_OPTIONS = (By.XPATH, "//div[@class='oxd-select-option']/span")
    DATE_OF_BIRTH_DROPDOWN = (By.XPATH, "(//div[@class='oxd-date-input']/input)[2]")
    DATE_OF_BIRTH_DATE_CALENDAR_WRAPPER_DATES = (
    By.XPATH, "//div[@class='oxd-calendar-wrapper']//div[@class='oxd-calendar-date-wrapper']")
    GENDER_SELECTION = (By.XPATH, "//div[@class='oxd-radio-wrapper']/label")
    SMOKER_CHECK_BOX = (By.XPATH, "(//div[@class='oxd-checkbox-wrapper']//input)[1]")
    MILITARY_SERVICE_INPUT = (
        By.XPATH, "//label[contains(text(),'Military Service')]/parent::div/following-sibling::div/input")
    BLOOD_TYPE_DROPDOWN = (By.XPATH, "//label[contains(text(),'Blood Type')]/parent::div/following-sibling::div//i")
    BLOOD_TYPE_DROPDOWN_OPTIONS = (By.XPATH, "//div[@class='oxd-select-option']/span")
    ATTACHMENT_ADD_BUTTON = (By.XPATH, "//div[@class='orangehrm-action-header']//button")
    UPLOAD_PHOTO_INPUT = (By.XPATH, "//input[@class='oxd-file-input']")
    COMMENT_SECTION = (By.XPATH, "//div/textarea")
    SAVE_BUTTON_THIRD = (By.XPATH, "(//button[@type='submit'])[3]")
    CANCEL_BUTTON_THIRD = (By.XPATH, "(//button[@type='button'])[3]")
    NATIONALITY_DROPDOWN_OPTIONS = (By.XPATH, "//div[@class='oxd-select-option']/span")
    MARITAL_STATUS_DROPDOWN_TEXTS = (
        By.XPATH, "//label[contains(text(),'Marital Status')]/parent::div/following-sibling::div/div/div/div")
    NATIONALITY_DROPDOWN_TEXTS = (
        By.XPATH, "//label[contains(text(),'Nationality')]/parent::div/following-sibling::div/div/div/div")
    DROP_BACK = (By.XPATH, "//div[@class='oxd-loading-spinner-container']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check()

    def check(self):
        """
        Checks the elements available on the page
        """
        self.go_to_my_info_page()
        assert "viewPersonalDetails" in self.fetch_current_url(), "URL is not containing viewPersonalDetails text!"
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.LOGO),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.FIRST_NAME_INPUT),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.MIDDLE_NAME_INPUT),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.SURNAME_INPUT),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.EMERGENCY_CONTACTS_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.DEPENDENTS_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.IMMIGRATION_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.JOB_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.SALARY_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.TAX_EXEMPTIONS_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.REPORT_TO_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.QUALIFICATIONS_TAB),
                                           message="LOGO is not visible for the Dashboard")
        self.fluent_wait(timeout=10).until(ec.visibility_of_element_located(self.MEMBERSHIPS_TAB),
                                           message="LOGO is not visible for the Dashboard")

    def go_to_my_info_page(self):
        """
        Navigates to the My Info Page
        """
        self.click_on_navbar_element(self.LEFT_NAVBAR_MY_INFO_PAGE)

    def choose_dropdown(self, selection: str = "", cursor=None):
        """
        Selects the specified option from the dropdown

        :param cursor: LOCATOR for each dropdown option
        :param selection: Text belongs to the chosen dropdown option
        """

        dropdown_elements = self.find_elements(cursor)
        navbar_element = list(filter(lambda x: self.fetch_element_text(x) == selection, dropdown_elements))
        self.click_element(navbar_element[0])

    def fill_personal_details(self,
                              first_name: str = None,
                              middle_name: str = None,
                              surname_name: str = None,
                              employee_id: str = None,
                              driver_license_number: str = None,
                              ssn_number: str = None,
                              sin_number: str = None,
                              nationality: str = None,
                              marital_status: str = None,
                              gender: str = None,
                              file_path_to_be_uploaded: str = None,
                              military_service: str = None,
                              smoker: bool = False,
                              blood_type: str = "A+",
                              comment: str = None
                              ) -> str:
        """
        Fills personal details on the page belongs to the user

        :param first_name: First name text
        :param middle_name: Middle Name text
        :param surname_name: Surname text
        :param employee_id: Employee Id text
        :param driver_license_number: Drive License Number text
        :param license_expiry_date: License Expiry Date text
        :param ssn_number: SSN Number text
        :param sin_number: Sin Number text
        :param nationality: Nationality text
        :param marital_status: Marital Status text
        :param date_of_birth: Date of Birth text
        :param gender: Gender text
        :param military_service: Military Service text
        :param file_path_to_be_uploaded: File to be uploaded
        :param smoker: Smoker Checkbox
        :param blood_type: Blood Type text
        :param comment: Comment content

        :return string
        """
        self.clear_keys(self.FIRST_NAME_INPUT)
        self.enter_keys(self.FIRST_NAME_INPUT, first_name)

        self.clear_keys(self.MIDDLE_NAME_INPUT)
        self.enter_keys(self.MIDDLE_NAME_INPUT, middle_name)

        self.clear_keys(self.SURNAME_INPUT)
        self.enter_keys(self.SURNAME_INPUT, surname_name)

        self.clear_keys(self.EMPLOYEE_ID_INPUT)
        self.enter_keys(self.EMPLOYEE_ID_INPUT, employee_id)

        self.clear_keys(self.DRIVER_LICENSE_NUMBER_INPUT)
        self.enter_keys(self.DRIVER_LICENSE_NUMBER_INPUT, driver_license_number)

        self.click_element(self.LICENSE_EXPIRY_DATE)
        dates_from_expiry_calendar = self.find_elements(self.LICENSE_EXPIRY_DATE_CALENDAR_WRAPPER_DATES)
        self.click_element(dates_from_expiry_calendar[5])

        self.clear_keys(self.SSN_NUMBER_INPUT)
        self.enter_keys(self.SSN_NUMBER_INPUT, ssn_number)

        self.clear_keys(self.SIN_NUMBER_INPUT)
        self.enter_keys(self.SIN_NUMBER_INPUT, sin_number)

        self.click_element(self.NATIONALITY_DROPDOWN)
        self.choose_dropdown(cursor=self.NATIONALITY_DROPDOWN_OPTIONS, selection=nationality)

        self.click_element(self.MARITAL_STATUS_DROPDOWN)
        self.choose_dropdown(cursor=self.MARITAL_STATUS_OPTIONS, selection=marital_status)

        self.click_element(self.DATE_OF_BIRTH_DROPDOWN)
        dates_from_expiry_calendar = self.find_elements(self.DATE_OF_BIRTH_DATE_CALENDAR_WRAPPER_DATES)
        self.click_element(dates_from_expiry_calendar[5])

        genders = self.find_elements(self.GENDER_SELECTION)
        gender_selection = list(filter(lambda gen: self.fetch_element_text(gen) == gender, genders))

        if gender != self.fetch_element_text(gender_selection[0]):
            self.click_element(gender_selection[0])

        self.clear_keys(self.MILITARY_SERVICE_INPUT)
        self.enter_keys(self.MILITARY_SERVICE_INPUT, military_service)

        if smoker:
            self.click_with_javascript_method(self.SMOKER_CHECK_BOX)

        self.click_element(self.BLOOD_TYPE_DROPDOWN)
        self.choose_dropdown(cursor=self.BLOOD_TYPE_DROPDOWN_OPTIONS, selection=blood_type)

        self.click_element(self.ATTACHMENT_ADD_BUTTON)
        self.fluent_wait(5).until(ec.presence_of_all_elements_located(self.COMMENT_SECTION))

        self.clear_keys(self.COMMENT_SECTION)
        self.enter_keys(self.COMMENT_SECTION, comment)

        self.enter_keys(self.UPLOAD_PHOTO_INPUT, file_path_to_be_uploaded)

        self.click_element(self.SAVE_BUTTON_THIRD)
        alert = self.fetch_alert_message()

        return alert
