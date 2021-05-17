# TODO 1: Добавить скиншоты при фейлах
# TODO 2: Добавить allure

import time
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement
from typing import Union
from Core.utils import get_project_root

class DriverCustom:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://uitestingplayground.com'

    def screen_shot(self, result_message: str):
        file_name = str(round(time.time() * 1000)) + ".png"
        path_to_save = get_project_root() / "Screenshots"
        try:
            if not path_to_save.is_dir():
                path_to_save.mkdir()
            logger.debug(self.driver.save_screenshot(str(path_to_save/file_name)))
            logger.info(f"Screenshot save to directory: {str(path_to_save)}. Name: {file_name}")
        except TimeoutException:
            logger.error("### Exception Occurred when taking screenshot")


    def go_to_page(self):
        logger.info(f"go to {self.base_url}")
        self.driver.get(self.base_url)

    def get_by_type(self, locator_type: str) -> By:
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'partial link':
            return By.PARTIAL_LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            logger.error(f"Locator type: {locator_type} not correct/supported")
            raise NotImplementedError('Нет такого By')

    def get_element(self, locator: str, locator_type: str = "css") -> WebElement:
        element = None
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_element(by_type, locator))
            logger.info(f'Element found with locator: {locator} and locatorType: {locator_type}')
            self.screen_shot(f'{locator}')
        except TimeoutException as e:
            logger.exception(f"Element not found with locator: {locator} and locatorType: {locator_type}")
            self.screen_shot(f'{locator}')
        return element

    def get_elements(self, locator: str, locator_type: str = "css") -> list[WebElement]:
        elements = None
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        try:
            elements = wait.until(lambda driver: self.driver.find_elements(by_type, locator))
            logger.info(f'Elements found with locator: {locator} and locatorType: {locator_type}')
        except TimeoutException:
            logger.exception(f"Elements not found with locator: {locator} and locatorType: {locator_type}")
            # self.screen_shot(f'{locator}')
        return elements

    def clear_the_element(self, locator: str, locator_type: str = "css"):
        element = self.get_element(locator, locator_type)
        element.clear()

    def send_keys_to(self, data: str, locator: str, locator_type: str = "css"):
        element = self.get_element(locator, locator_type)
        try:
            element.send_keys(data)
            logger.info(f"Sent data to element with locator: {locator} and locatorType: {locator_type}")
        except TimeoutException:
            logger.info(f"Cannot send data to element with locator: {locator} and locatorType: {locator_type}")

    def wait_for_element_to_be_clickable(self,
                                         locator: str,
                                         locator_type: str = "id",
                                         timeout: Union[int, float] = 10,
                                         poll_frequency: Union[int, float] = 0.5) -> bool:
        by_type = self.get_by_type(locator_type)
        try:
            logger.info(f"Waiting for maximum: {timeout} seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            is_clickable = wait.until(EC.element_to_be_clickable((by_type,
                                                                  locator)))
            logger.info(f"Element {locator} appeared on the web page. locatorType {locator_type}")
        except TimeoutException:
            logger.info(f"Element {locator} not appeared on the web page. LocatorType {locator_type}")
            is_clickable = False
        return is_clickable

    def scroll_into_view(self, locator: str, locator_type: str = "css"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info(f"Scrolled to element with locator: {locator} and locatorType: {locator_type}")
        except:
            # from pdb import set_trace; set_trace()
            logger.exception(f"Can't be scrolled to element with locator: {locator} and locatorType: {locator_type}")
