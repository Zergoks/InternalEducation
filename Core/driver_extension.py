import time
from abc import abstractmethod
from typing import List
from typing import Union

from loguru import logger
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementNotSelectableException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import JavascriptException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from Core.utils import get_project_root


class DriverExtension:
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def at_page(self):
        pass

    def screen_shot(self, result_message: str = None):
        """Developed for taking custom screenshot"""
        file_name = str(round(time.time() * 1000)) + ".png"
        path_to_save = get_project_root() / "Reports" / "Screenshots"
        if not path_to_save.is_dir():
            path_to_save.mkdir()
        if self.driver.save_screenshot(str(path_to_save / file_name)):
            logger.info(
                f"Screenshot save to directory: {str(path_to_save)}. Name: {file_name}",
            )
        else:
            logger.error("### Exception Occurred when taking screenshot")

    def get_element(
        self,
        locator_model: tuple,
        timeout: Union[int, float] = 10,
    ) -> WebElement:
        element = None
        locator, by_type = locator_model
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(
                lambda driver: self.driver.find_element(by_type, locator),
            )
            logger.info(
                f"Element found with locator: {locator} and locatorType: {by_type}",
            )
        except TimeoutException:
            logger.error(
                f"Element not found with locator: {locator} and locatorType: {by_type}",
            )
        return element

    def get_elements(
        self,
        locator_model: tuple,
        timeout: Union[int, float] = 10,
    ) -> List[WebElement]:
        elements = None
        wait = WebDriverWait(self.driver, timeout)
        locator, by_type = locator_model
        try:
            elements = wait.until(
                lambda driver: self.driver.find_elements(by_type, locator),
            )
            logger.info(
                f"Elements found with locator: {locator} and locatorType: {by_type}",
            )
        except TimeoutException:
            logger.error(
                f"Elements not found with locator: {locator} and locatorType: {by_type}",
            )
        return elements

    def clear_the_element(self, locator_model: tuple):
        element = self.get_element(locator_model)
        element.clear()
        logger.info(f"Cleared element with locator_model: {locator_model}")

    def send_keys_to(self, data: str, locator_model: tuple):
        element = self.get_element(locator_model)
        try:
            element.send_keys(data)
            logger.info(f"Sent data to element with locator_model: {locator_model}")
        except TimeoutException:
            logger.error(
                f"Cannot send data to element with locator_model: {locator_model}",
            )

    def wait_for_element_to_be_clickable(
        self,
        locator_model: tuple,
        timeout: Union[int, float] = 10,
        poll_frequency: Union[int, float] = 0.5,
    ):
        element = None
        locator, by_type = locator_model
        try:
            logger.info(
                f"Waiting for maximum: {timeout} seconds for element to be clickable",
            )
            wait = WebDriverWait(
                self.driver,
                timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                    ElementNotInteractableException,
                ],
            )
            element = wait.until(
                ec.element_to_be_clickable(
                    (
                        by_type,
                        locator,
                    ),
                ),
            )
            logger.info(
                f"Element {locator} appeared on the web page. locatorType {by_type}",
            )
        except TimeoutException:
            logger.info(
                f"Element {locator} not appeared on the web page. LocatorType {by_type}",
            )
        return element

    def wait_until_page_is_fully_loaded(self, timeout: Union[int, float] = 10) -> bool:
        try:
            logger.info(
                f"Waiting for maximum: {timeout} seconds for complete loading of the page"
            )
            WebDriverWait(self.driver, timeout,).until(
                lambda driver: self.driver.execute_script("return document.readyState")
                == "complete"
            )
            logger.info("The page is fully loaded")
        except TimeoutException:
            logger.info("Page state is not complete")
            return False
        return True

    def scroll_into_view(self, locator_model: tuple):
        try:
            element = self.get_element(locator_model)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info(f"Scrolled to element with locator_model: {locator_model}")
        except JavascriptException:
            logger.exception(
                f"Can't be scrolled to element with locator_model: {locator_model}",
            )

    def click_on_element(self, locator_model: tuple) -> None:
        element = self.wait_for_element_to_be_clickable(locator_model)
        self.wait_until_page_is_fully_loaded()
        element.click()
        logger.info(f"Clicked on element with locator_model: {locator_model}")

    def get_element_attribute(self, attribute, locator_model: tuple):
        element = self.get_element(locator_model)
        element_value = element.get_attribute(attribute)
        if element_value:
            logger.info(
                f"Element attribute {attribute} found with locator_model: {locator_model}",
            )
        else:
            logger.warning(
                f"Element attribute {attribute} NOT found with locator_model: {locator_model}",
            )
        return element_value

    def is_element_clickable(self, locator_model: tuple):
        element = self.wait_for_element_to_be_clickable(locator_model)
        if element:
            return True
        return False

    def is_element_visible(self, locator_model: tuple, timeout=10):
        element = self.get_element(locator_model, timeout)
        if element is None or element.is_displayed() is False:
            logger.info(f"Element with locator_model {locator_model} is not visible")
            return False
        logger.info(f"Element with locator_model {locator_model} is visible")
        return True

    def is_alert_present(self, timeout=10) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.alert_is_present())
        except TimeoutException:
            logger.info("alert not found")
            return False
        logger.info("alert found")
        return True

    def switch_to_alert(self):
        logger.info("switch to alert")
        return self.driver.switch_to.alert

    def get_element_text(self, locator_model) -> str:
        element = self.get_element(locator_model)
        text = element.text
        logger.info(f"Element with locator_model: {locator_model} and text: {text}")
        return text