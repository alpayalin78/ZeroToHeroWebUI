import logging

from base import (JsonFormatter, detailed_formatter, configuration, AllureHandler,
                  GermanAddress, TurkeyAddress)
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import glamor as allure
import pytest
import os


@pytest.fixture(scope="session")
def initialize_chrome_driver() -> dict:
    return {"name": "Chrome"}


@pytest.fixture(scope="session", autouse=True)
def maximize_window() -> bool:
    return True


@pytest.fixture(scope="session", autouse=True)
def user_information() -> dict:
    return {"username": "", "password": ""}


@pytest.fixture
def driver_test(initialize_chrome_driver, request: pytest.FixtureRequest):
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

        service = Service()
        driver = webdriver.Chrome(service=service, options=options)

        if request.config.getoption("incognito"):
            options.add_argument("--incognito")

        if maximize_window:
            driver.maximize_window()

        yield driver

        def finalizer():
            try:
                report_dir = request.config.getoption('--alluredir')
                with open(report_dir, "w") as f:
                    for key, value in driver.capabilities.items():
                        f.write(f"{key}={value}\n")
            except Exception as e:
                logging.exception(e, exc_info=True)

        request.addfinalizer(finalizer)


@pytest.fixture
@allure.title("Logger")
def logger(request: pytest.FixtureRequest):
    logfile = request.config.getoption('--logfile')

    _ = configuration(logfile=logfile)
    allure_handler = AllureHandler()

    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)

    if allure_handler not in logger.handlers:
        logger.log(logging.INFO, 'Adding Allure logger')
        logger.addHandler(allure_handler)

    fh = logging.FileHandler(f"{logfile}\\{request.node.originalname}.log", encoding="utf8")
    fh.setFormatter(detailed_formatter)
    jh = logging.FileHandler(f"{logfile}\\json_view\\{request.node.originalname}.log", encoding="utf8")
    jh.setFormatter(JsonFormatter())

    logger.addHandler(fh)
    logger.addHandler(jh)
    yield logger

    logger.removeHandler(allure_handler)
    logger.removeHandler(fh)
    logger.removeHandler(jh)


@pytest.fixture
@allure.title.setup("Initializing test configurations", hidden=True)
@allure.title.teardown("Test is finished", hidden=True)
def initialize_web_ui(request, logger, driver_test):
    request.cls.logger = logger
    request.cls.driver = driver_test


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--logfile', action='store', default='log', help="Log file path"
    )
    parser.addoption(
        '--incognito', action='store', type=lambda x: (str(x).lower() == 'true'), default=False,
        help='Incognito mode option'
    )
    parser.addoption(
        '--environment', action='store', type=str, default="turkish",
        help='environment selection'
    )


def pytest_generate_tests(metafunc: pytest.Metafunc):
    match metafunc.config.getoption('--environment'):
        case "german":
            data = GermanAddress()
        case "turkish":
            data = TurkeyAddress()
        case _:
            raise EnvironmentError("Unused environment option!")
    try:
        funcarglist = metafunc.cls.generate_parameters(data=data)[metafunc.function.__name__]
        argnames = sorted(funcarglist[0])
        metafunc.parametrize(argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist])
    except Exception as e:
        logging.exception(f"Error: {e}, Path: {metafunc.definition.path}", exc_info=True)


def pytest_sessionstart(session: pytest.Session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "result_" + result.when, result)

    if result.when == "call" or result.outcome == "failed":
        item.session.results[item] = result
    elif result.when == "setup":
        item.cls.__doc__ = item.cls.description(**item.funcargs)
