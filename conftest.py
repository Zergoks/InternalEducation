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
    driver = None
    driver = create_local_driver(config)
    request.instance.driver = driver
    driver.delete_all_cookies()
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()


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
