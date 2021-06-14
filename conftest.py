import sys

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from loguru import logger
import logging
from pathlib import Path
from Core.utils import list_of_random_strings

PATH_TO_GECKODRIVER = 'Core/drivers/geckodriver.exe'
AMOUNT_RANDOM_STRINGS = 3

string_generator = list_of_random_strings(AMOUNT_RANDOM_STRINGS)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--browser_ver", action="store", default="")
    parser.addoption("--headless", action="store", default=False)
    parser.addoption("--env", action="store", default="test")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--remote", action="store", default=False)
    parser.addoption("--hub", action="store", default="localhost")


@pytest.fixture()
def environment(request):
    yield request.config.getoption('--env')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    hub = request.config.getoption("--hub")
    headless = False
    remote = False
    if request.config.getoption("--headless"):
        headless = True
    if request.config.getoption("--remote"):
        remote = True

    return {
        "version": version,
        "browser": browser,
        "headless": headless,
        "remote": remote,
        "hub": hub
    }


def get_chrome_options(config):
    options = ChromeOptions()
    options.headless = config["headless"]
    return options


def get_firefox_options(config):
    options = FirefoxOptions()
    options.headless = config["headless"]
    return options


def create_local_driver(config):
    driver = None
    if config["browser"] == "chrome":
        driver_manager = ChromeDriverManager()
        options = get_chrome_options(config)
        driver = webdriver.Chrome(executable_path=driver_manager.install(), options=options)
    elif config["browser"] == "firefox" or "ff":
        driver_manager = GeckoDriverManager("82.0")
        options = get_firefox_options(config)
        driver = webdriver.Firefox(executable_path='Core/drivers/geckodriver.exe', options=options)
    return driver


def create_remote_driver(config):
    if config["browser"] == "chrome":
        options = get_chrome_options(config)
        options.add_argument("--disable-dev-shm-usage")  # overcome limited resource problems
        # options.add_argument("--start-maximized")  # open Browser in maximized mode
        # options.add_argument("--no-sandbox")  # bypass OS security model
        # options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # options.add_experimental_option('useAutomationExtension', False)
    else:
        options = get_firefox_options(config)
    capabilities = {"version": config["version"],
                    "acceptInsecureCerts": True,
                    "screenResolution": "1280x1024x24"}
    return webdriver.Remote(command_executor="http://{}:4444/wd/hub".format(config["hub"]),
                            options=options,
                            desired_capabilities=capabilities)


# @pytest.fixture(scope="function")
# def driver(request, config):
#     """Вариант проброса драйвера через request.addfinalizer и return"""
#     driver = None
#     driver = create_local_driver(config)
#     request.instance.driver = driver
#     driver.delete_all_cookies()
#     driver.maximize_window()
#     driver.implicitly_wait(3)
#
#     def tear_down():
#         driver.quit()
#
#     request.addfinalizer(tear_down)
#     return driver


@pytest.fixture()
def driver(request, config):
    """Вариант проброса драйвера через yield"""
    if config["remote"]:
        driver = create_remote_driver(config)
    else:
        driver = create_local_driver(config)
        request.instance.driver = driver
        driver.delete_all_cookies()
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.fixture(scope='function', params=string_generator)
def generated_mix_string(request):
    yield request.param


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    """Скриншот при падении теста с аттачем к allure"""
    outcome = yield
    rep = outcome.get_result()
    # marker = item.get_closest_marker("ui")
    # if marker:
    if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
        try:
            allure.attach(item.instance.driver.get_screenshot_as_png(),
                          name=item.name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
            logger.error("screenshot failed")


@pytest.fixture(autouse=True)
def create_log_file(request):
    log_level = request.config.getoption("--log_level")

    path_to_logs = Path.cwd() / "Reports" / "Logs"
    if log_level == 'DEBUG':
        logger.add(path_to_logs / "{time}_debug.log",
                   level=logging.DEBUG,
                   format="{level}: {message}")
    if log_level == 'INFO':
        logger.add(path_to_logs / "{time}_info.log",
                   level=logging.INFO,
                   format="{level}: {message}")

    logger.add(path_to_logs / "{time}_error.log",
               level=logging.ERROR)
