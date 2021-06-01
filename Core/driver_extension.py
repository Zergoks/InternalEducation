# TODO 3: wait_for_element_to_be_clickable может вынести фикстурой? или отельную фикстуру на ожидания

from abc import abstractmethod
from typing import Union, List

from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement

from Core.utils import get_project_root
import time


class DriverCustom:

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def at_page(self):
        pass

    def screen_shot(self, result_message: str = None):
        """Делаем скриншот ui В произвольном месте
        Авто скриншот вынесен в conftest.py на фейлы с аттачем к аллюру"""
        file_name = str(round(time.time() * 1000)) + ".png"
        path_to_save = get_project_root() / "Reports" / "Screenshots"
        try:
            if not path_to_save.is_dir():
                path_to_save.mkdir()
            self.driver.save_screenshot(str(path_to_save / file_name))
            logger.info(f"Screenshot save to directory: {str(path_to_save)}. Name: {file_name}")
        except:
            logger.error("### Exception Occurred when taking screenshot")
            raise

    def get_element(self, locator: str, by_type: By = By.XPATH) -> WebElement:
        element = None
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_element(by_type, locator))
            logger.info(f'Element found with locator: {locator} and locatorType: {by_type}')
        except TimeoutException:
            logger.error(f"Element not found with locator: {locator} and locatorType: {by_type}")
        return element

    def get_elements(self, locator: str, by_type: By = By.XPATH, timeout: Union[int, float] = 10) -> List[WebElement]:
        elements = None
        wait = WebDriverWait(self.driver, timeout)
        try:
            elements = wait.until(lambda driver: self.driver.find_elements(by_type, locator))
            logger.info(f'Elements found with locator: {locator} and locatorType: {by_type}')
        except TimeoutException:
            logger.error(f"Elements not found with locator: {locator} and locatorType: {by_type}")
        return elements

    def clear_the_element(self, locator: str, by_type: By = By.XPATH):
        element = self.get_element(locator, by_type)
        element.clear()

    def send_keys_to(self, data: str, locator: str, by_type: By = By.XPATH):
        element = self.get_element(locator, by_type)
        try:
            element.send_keys(data)
            logger.info(f"Sent data to element with locator: {locator} and locatorType: {by_type}")
        except TimeoutException:
            logger.error(f"Cannot send data to element with locator: {locator} and locatorType: {by_type}")

    def wait_for_element_to_be_clickable(self,
                                         locator: str,
                                         by_type: By = By.XPATH,
                                         timeout: Union[int, float] = 10,
                                         poll_frequency: Union[int, float] = 0.5):
        element = None
        try:
            logger.info(f"Waiting for maximum: {timeout} seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementNotInteractableException,
                                                     ])
            element = wait.until(ec.element_to_be_clickable((by_type,
                                                             locator)))

            logger.info(f"Element {locator} appeared on the web page. locatorType {by_type}")
        except TimeoutException:
            logger.info(f"Element {locator} not appeared on the web page. LocatorType {by_type}")
        return element

    def scroll_into_view(self, locator: str, by_type: By = By.XPATH):
        try:
            element = self.get_element(locator, by_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info(f"Scrolled to element with locator: {locator} "
                        f"and locatorType: {by_type}")
        except:
            # from pdb import set_trace; set_trace()
            logger.exception(f"Can't be scrolled to element with locator: {locator} "
                             f"and locatorType: {by_type}")

    def click_on_element(self, locator: str, by_type: By = By.XPATH) -> None:
        element = self.wait_for_element_to_be_clickable(locator, by_type)
        element.click()
        logger.info(f"Clicked on element with locator: {locator} "
                    f"and locatorType: {by_type}")

    def get_element_attribute(self, attribute, locator, by_type: By = By.XPATH):
        element = self.get_element(locator, by_type)
        element_value = element.get_attribute(attribute)
        if element_value:
            logger.info(f"Element attribute {attribute} found with locator: {locator} and locatorType: {by_type}")
        else:
            logger.warning(f"Element attribute {attribute} NOT found with locator: {locator} "
                           f"and locatorType: {by_type}")
        return element_value

    def is_element_clickable(self, locator, by_type: By = By.XPATH):
        element = self.wait_for_element_to_be_clickable(locator, by_type)
        if element:
            return True
        return False

    def is_element_visible(self, locator, by_type: By = By.XPATH, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(ec.visibility_of_element_located((by_type, locator)))
            logger.info(f"Element {locator} with and locatorType: {by_type} is visible")
            return True
        except TimeoutException:
            logger.info(f"Element {locator} with and locatorType: {by_type} is not visible")
            return False

    def is_alert_present(self) -> bool:
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(ec.alert_is_present())
        except TimeoutException:
            logger.info(f"alert not found")
            return False
        logger.info(f"alert found")
        return True

    def switch_to_alert(self):
        logger.info("switch to alert")
        return self.driver.switch_to.alert
