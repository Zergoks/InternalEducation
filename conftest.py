# TODO 1: добавить изменения уровня логирования из параметров --log_level

import sys
import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from loguru import logger
import logging
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--browser_ver", action="store", default="")
    parser.addoption("--headless", action="store", default=False)
    parser.addoption("--env", action="store", default="test")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture()
def environment(request):
    yield request.config.getoption('--env')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    headless = False
    if request.config.getoption("--headless"):
        headless = True

    return {
        "version": version,
        "browser": browser,
        "headless": headless,
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
        driver_manager = GeckoDriverManager()
        options = get_firefox_options(config)
        driver = webdriver.Firefox(executable_path=driver_manager.install(), options=options)
    return driver


@pytest.fixture()
def driver(request, config):
    "Вариант проброса драйвера через request.addfinalizer и return"
    driver = None
    driver = create_local_driver(config)
    request.instance.driver = driver
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def tear_down():
        driver.quit()

    request.addfinalizer(tear_down)
    yield driver

# @pytest.fixture()
# def driver(request, config):
#     "Вариант проброса драйвера через yield"
#     driver = None
#     driver = create_local_driver(config)
#     request.instance.driver = driver
#     driver.delete_all_cookies()
#     driver.maximize_window()
#     driver.implicitly_wait(3)
#
#     yield driver


@pytest.fixture(scope='session', autouse=True)
def create_log_file():
    """The rotation check is made before logging each message.
    If there is already an existing file with the same name that the file to be created,
    then the existing file is renamed by appending the date to its basename to prevent file overwriting.
    This parameter accepts:
    Examples: "100 MB", "0.5 GB", "1 month 2 weeks", "4 days", "10h",
    "monthly", "18:00", "sunday", "w0", "monday at 12:00
    can be compression='zip' """
    info_handler = logger.add(Path.cwd() / 'logs' / "start_in_{time}_info.log",
                              level=logging.INFO,
                              format="{level}: {message}")
    error_handler = logger.add(Path.cwd() / 'logs' / "start_in_{time}_error.log",
                               level=logging.ERROR)
