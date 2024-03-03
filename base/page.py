import json

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from time import ctime, time
import re


class BasePage:
    SIDE_BAR = (By.XPATH, "//a[@class='oxd-main-menu-item']")
    ALERT_POP_UP = (By.XPATH, "(//div[@id='oxd-toaster_1']//p)[1]")
    COUNTRIES_SELECTIONS = (By.XPATH, "//div[@class='a-popover-wrapper']//ul/li")

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.timeout = 10

    def fluent_wait(self, timeout: float = 10., poll_frequency=0.5, ignored_exceptions=None) -> WebDriverWait:
        """
        Returns WebDriverWait object

        :param timeout: Time amount to be used in waiting
        :param poll_frequency: Frequency rate
        :param ignored_exceptions: Ignore the exceptions except timeout
        :return: WebDriverWait
        """
        return WebDriverWait(driver=self.driver, timeout=timeout,
                             poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)

    def fetch_current_url(self) -> str:
        """
        Returns current URL

        :return: str
        """
        return self.driver.current_url

    def is_element_clickable(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is clickable

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        try:
            return bool(self.fluent_wait(timeout=timeout).until(ec.element_to_be_clickable(cursor)))

        except TimeoutException:
            return False

    def find_element(self, locator) -> WebElement:
        """
        Find element for the given LOCATOR

        :param locator: Locator
        :return: WebElement
        """
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                              message=f"Element <{locator}> is not present")

    def find_elements(self, locator) -> list[WebElement]:
        """
        Find elements for the given LOCATOR

        :param locator: Locator
        :return: list
        """
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))

    def scroll_to_element(self, cursor) -> None:
        """
        Scrolls to the given element on the page

        :param cursor: Locator or Web Element
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.driver.execute_script("arguments[0].scrollIntoView(false)", element)

    def click_element(self, cursor) -> None:
        """
        Clicks to the given element

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_element_clickable(element)
        self.scroll_to_element(element)
        element.click()

    def is_element_displayed(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is displayed

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        if isinstance(cursor, WebElement):
            return cursor.is_displayed()

        try:
            element = self.fluent_wait(timeout=timeout).until(ec.presence_of_element_located(cursor))
            return element.is_displayed()

        except TimeoutException:
            return False

    def click_on_navbar_element(self, locator: tuple) -> None:
        """
        Clicks on navbar element

        :param locator: Collection of the menu element's locator
        """
        navbar_elements = self.find_elements(self.SIDE_BAR)
        navbar_element = list(filter(lambda x: locator[1] == re.sub("[^A-Za-zğüşöçıİĞÜŞÖÇ/\s]",
                                                                    "", x.accessible_name), navbar_elements))[0]
        self.is_element_displayed(navbar_element)
        self.is_element_clickable(navbar_element)
        self.click_element(navbar_element)

    def fetch_element_text(self, cursor) -> str:
        """
        Returns element text

        :param cursor: Locator or Web Element
        :return: str
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        return element.text

    def choose_dropdown(self, selection, cursor):
        """
        Selects the specified option from the dropdown

        :param cursor: LOCATOR for each dropdown option
        :param selection: Text belongs to the chosen dropdown option
        """

        dropdown_elements = self.find_elements(cursor)
        navbar_element = list(filter(lambda x: self.fetch_element_text(x) == selection, dropdown_elements))
        self.click_element(navbar_element[0])

    def click_with_javascript_method(self, cursor) -> None:
        """
        Clicks to the given element by javascript method

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_element_clickable(element)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click()", element)

    def is_enabled(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is enabled

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        if isinstance(cursor, WebElement):
            return cursor.is_enabled()
        try:
            element = self.fluent_wait(timeout=timeout).until(ec.presence_of_element_located(mark))
            return element.is_enabled()
        except TimeoutException:
            return False

    def enter_keys(self, cursor, text) -> None:
        """
        Enters given text to the input

        :param cursor: Locator or WebElement
        :param text: Given text
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_enabled(element)
        self.scroll_to_element(element)
        element.send_keys(text)

    def clear_keys(self, cursor) -> None:
        """
        Clears the entered input

        :param cursor: Locator or WebElement
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        self.is_enabled(element)
        self.scroll_to_element(element)
        element.clear()

    def is_element_enabled(self, cursor, timeout=10.) -> bool:
        """
        Checks if the element is enabled

        :param cursor: Locator or Web Element
        :param timeout: Time amount to be used in waiting
        :return: bool
        """
        if isinstance(cursor, WebElement):
            return cursor.is_enabled()

        try:
            element = self.fluent_wait(timeout=timeout).until(ec.presence_of_element_located(cursor))
            return element.is_enabled()

        except TimeoutException:
            return False

    def fetch_alert_message(self) -> str:
        """
        Fetches the alert message
        :return: str
        """
        self.fluent_wait(10).until(ec.presence_of_element_located(self.ALERT_POP_UP))
        alert_message = self.fetch_element_text(self.find_element(self.ALERT_POP_UP))

        return alert_message

    def take_screenshot(self, cursor, color: str, effect_time=.3, thickness=3, radius=8) -> None:
        """
        Takes screenshot of the specified element

        :param cursor: Locator or Web Element
        :param color: Border color
        :param effect_time: Shows how long it's going to be on the screen
        :param thickness: Border thickness
        :param radius: Border radius
        """
        if isinstance(cursor, WebElement):
            element = cursor

        else:
            element = self.find_element(cursor)

        if (element.tag_name == "input" or element.tag_name == "textarea") and element.get_attribute("value") == "":
            return None

        self.scroll_to_element(element)
        self.driver = element.parent
        original_style = element.get_attribute('style')

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

        apply_style(f"border: {thickness}px solid {color}; border-radius: {radius}px;")
        self.static_wait(effect_time)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=ctime(time()).replace(":", "_"),
                      attachment_type=AttachmentType.PNG)
        apply_style(original_style)

    def static_wait(self, timeout=3.0) -> None:
        """
        Static wait on the current page

        :param timeout: Time amount to be used in waiting
        """
        try:
            WebDriverWait(self.driver, timeout).until(lambda _: False)
        except TimeoutException:
            pass

    @classmethod
    def attach_json_to_report(cls, json_file: dict | list, name: str):
        """
        Attaches JSON to allure report

        :param json_file: JSON File
        :param name: Attachment name
        """
        allure.attach(json.dumps(json_file, indent=4, sort_keys=True, default=str, ensure_ascii=False),
                      name=name,
                      attachment_type=AttachmentType.JSON)

    @staticmethod
    def attach_html_to_report(html_file: str, name: str):
        """
        Attaches Html page to allure report

        :param html_file: HTML File as string
        :param name: Attachment name
        """
        allure.attach(html_file,
                      name=name,
                      attachment_type=AttachmentType.HTML)

    @staticmethod
    def dict_to_html(dict_files: list[dict], title: str, diff: list = None) -> str:
        """
        Generates Html page from dictionary to depict as table

        :param dict_files: List of dictionary to be used in data table
        :param diff: List of columns
        :param title: Title to be shown in the Html page

        :return: str
        """
        if len(dict_files) < 1:
            return """<h1> No Result Found </h1>"""

        differences = [{}] * len(dict_files)
        if diff is not None:
            for index, row in enumerate(diff):
                diff_dict = {}
                for dif in row:
                    if dif:
                        col, msg = dif.split("]")
                        diff_dict[col[1:]] = msg
                differences.insert(index, diff_dict)

        headers = ['<th>' + header + '</th>' for header in dict_files[0].keys()]
        data = ""
        for index, file in enumerate(dict_files):
            diff_dict = differences[index]
            data += '<tr align="center">'
            for key, value in file.items():
                if key in diff_dict:
                    data += '<td style="background-color: #FFCCCC;"><pre>' + str(diff_dict[key]).replace("<", "&lt;"). \
                        replace(">", "&gt;") + '</pre></td>'
                else:
                    data += '<td><pre>' + str(value).replace("<", "&lt;").replace(">", "&gt;") + '</pre></td>'
            data += "</tr>"
        style = """
        table, th, td {border: 1px solid black;  border-collapse: collapse;}
        th, td {padding: 10px 20px;}
        table {font-family: "Helvetica Neue", Helvetica, sans-serif; border-radius: 25px;}
        thead {background: SteelBlue; color: white;}
        tbody tr:nth-child(even) {background: WhiteSmoke;}
        pre {overflow: auto; scrollbar-width: none; max-height: 100px; max-width: 500px;}
        """
        html = """
        <meta charset="UTF-8">
        <style>
        {style}
        </style>
        <h1>{title}</h1>
        <table style="width:100%">
        <thead>
          <tr align="center">
            {headers}
          </tr>
        </thead>
        <tbody>
          {data}
        </tbody>
        </table>
        """
        return html.format(style=style, title=title, headers=''.join(headers), data=data)

    @staticmethod
    def add_br_tags(text) -> str:
        """
        Adds <br> tags if "#########" exists in the given text

        :param text: Text that is going to be splitted and row jumped.

        :return str:
        """
        formatted_text = text

        if "#########" in str(text):
            lines = text.split('\n')
            formatted_text = ""

            for line in lines:
                if "#########" not in line:
                    formatted_text += f"<br>{line.strip()}"

        return formatted_text

    @staticmethod
    def define_steps(step_list) -> str:
        """ Defines steps used in description of Allure Report
        :param step_list: Step List

        :return str:
        """
        step_list_to_be_returned = []

        for idx, step_list_element in enumerate(step_list):
            if idx < 9:
                element_step = f"""        
                    <tr>
                        <td>0{idx + 1}. {BasePage.add_br_tags(step_list_element)}</td>
                    </tr>"""
            else:
                element_step = f"""        
                    <tr>
                        <td>{idx + 1}. {BasePage.add_br_tags(step_list_element)}</td>
                    </tr>"""

            step_list_to_be_returned.append(element_step)

        return " ".join([step for step in step_list_to_be_returned])

    @staticmethod
    def define_parameters(parameters_list) -> str:
        """ Defines parameters used in description of Allure Report
        :param parameters_list: Parameter List

        :return str:
        """
        parameters_list_to_be_returned = []

        for parameters_list_element in parameters_list:
            element_step = f"""
            <tr>
                <strong><td>{parameters_list_element[0]}</td></strong>
                <td>{BasePage.add_br_tags(parameters_list_element[1])}</td>
            </tr>
            """
            parameters_list_to_be_returned.append(element_step)

        return " ".join([parameter for parameter in parameters_list_to_be_returned])

    @staticmethod
    def description_handler(test_case_name: str = None, test_case_aims: str = None,
                            expected_result: str = None,
                            parameters_list: tuple = None, step_list: list = None) -> str:
        """
        Gathers all the information needed to create a HTML versioned description for Allure Report.
        :param test_case_name: Test Case Name
        :param test_case_aims: Test Case Aim
        :param expected_result: Expected Result
        :param parameters_list: Parameter List
        :param step_list: Step List

        :return str:
        """

        report_str = f"""<html>
                            <head>
                                <title>Test Case Details</title>
                            </head>
                                <style>
                                    table {{
                                        table-layout: fixed;
                                        width: 100%;
                                    }}
                                    th, td {{
                                        width: 25%;
                                        word-wrap: break-word;
                                    }}
                                </style>
                            <body>
                                <table border="1">
                                    <tr>
                                        <strong><th colspan="2">Test Case Details</th></strong>
                                    </tr>
                                    <tr>
                                        <strong><td>Test Case Name</td></strong>
                                        <strong><td>{BasePage.add_br_tags(text=test_case_name)}</td></strong>
                                    </tr>
                                    <tr>
                                        <td>Test Case Aims</td>
                                        <td>{BasePage.add_br_tags(text=test_case_aims)}</td>
                                    </tr>
                                </table>

                                <table border="1">
                                    <tr>
                                        <strong><th>Parameters</th></strong>
                                    </tr>
                                    {BasePage.define_parameters(parameters_list=parameters_list)}
                                </table>

                                <table border="1">
                                    <tr>
                                        <th>Steps</th>
                                    </tr>
                                    {BasePage.define_steps(step_list=step_list)}
                                </table>

                                <table border="1">
                                    <tr>
                                        <th>Expected Result</th>
                                    </tr>
                                    <tr>
                                        <td>{BasePage.add_br_tags(text=expected_result)}</td>
                                    </tr>
                                </table>
                            </body>
                            </html>
                        """
        return report_str
