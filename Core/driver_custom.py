# TODO 1: Добавить скиншоты при фейлах

import os
import sys
import time
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC


class DriverCustom:
    logger.add(sys.stderr, format="{time}.{level}:{message}", level='ERROR')

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def screen_shot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../Screenshots/"
        relative_file_name = screenshot_directory + file_name
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            logger.info("Screenshot save to directory: " + destination_file)
        except:
            logger.error("### Exception Occurred when taking screenshot")

    def go_to_page(self):
        logger.info(f"go to {self.base_url}")
        self.driver.get(self.base_url)

    def get_by_type(self, locator_type) -> By:
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
            raise NotImplementedError

    def get_element(self, locator: str, locator_type: str ="css"):
        element = None
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_element(by_type, locator))
            logger.info(f'Element found with locator: {locator} and locatorType: {locator_type}')
        except TimeoutException as e:
            logger.exception(f"Element not found with locator: {locator} and locatorType: {locator_type}")
            # self.screen_shot(f'{locator}')
        return element

    def get_elements(self, locator, locator_type="css"):
        element = None
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_elements(by_type, locator))
            logger.info(f'Elements found with locator: {locator} and locatorType: {locator_type}')
        except TimeoutException:
            logger.exception(f"Elements not found with locator: {locator} and locatorType: {locator_type}")
            # self.screen_shot(f'{locator}')
        return element

    def clear_the_element(self, locator, locator_type="css"):
        element = self.get_element(locator, locator_type)
        element.clear()

    def send_keys_to(self, data, locator, locator_type="css"):
        element = self.get_element(locator, locator_type)
        try:
            element.send_keys(data)
            logger.info(f"Sent data to element with locator: {locator} and locatorType: {locator_type}")
        except TimeoutException:
            logger.info(f"Cannot send data to element with locator: {locator} and locatorType: {locator_type}")

    def wait_for_element_to_be_clickable(self, locator, locator_type="id",
                                         timeout=10, poll_frequency=0.5) -> bool:
        by_type = self.get_by_type(locator_type)
        try:
            logger.info(f"Waiting for maximum: {timeout} seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=poll_frequency,
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

    def scroll_into_view(self, locator, locator_type="css"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator, locator_type)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            logger.info("Scrolled to element with locator: " + locator +
                          " locatorType: " + locator_type)
        except:
            logger.exception("Can't be scrolled to element with locator: " + locator +
                          " locatorType: " + locator_type)
            # print_stack()

