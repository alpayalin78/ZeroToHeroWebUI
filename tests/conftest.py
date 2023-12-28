from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
import pytest
import os


@pytest.fixture(scope="session", autouse=True)
def initialize_chrome_driver() -> dict:
    return {"name": "Chrome"}


@pytest.fixture(scope="session", autouse=True)
def maximize_window() -> bool:
    return True


@pytest.fixture(scope="session", autouse=True)
def user_information() -> dict:
    return {"username": "Admin", "password": "admin123"}


@pytest.fixture
def driver_test(initialize_chrome_driver):
    if initialize_chrome_driver["name"] == "Chrome":
        options = webdriver.ChromeOptions()
        # opts.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920x1080')
        options.add_argument("disable-blink-features")
        options.add_argument("disable-blink-features=AutomationControlled")
        prefs = {'download.default_directory': f"{os.getcwd()}", "download.prompt_for_download": False}
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver_path = "C:/Users/alpay.alin/ynt-kolaygelsin-automation-webui/chromedriver.exe"
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        if maximize_window:
            driver.maximize_window()

        yield driver

        driver.delete_all_cookies()
        driver.close()
        driver.quit()
