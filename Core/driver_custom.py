# TODO 1: Добавить скиншоты при фейлах

import sys
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class DriverCustom:
    logger.add(sys.stderr, format="{time} {level} {message}", level='DEBUG')

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
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
        return False

    def get_element(self, locator, locator_type="css"):
        element = None
        locator_type = locator_type.lower()
        by_type = self.get_by_type(locator_type)
        wait = WebDriverWait(self.driver, 10)
        try:
            element = wait.until(lambda driver: self.driver.find_element(by_type, locator))
            logger.info(f'Element found with locator: {locator} and locatorType: {locator_type}')
        except:
            logger.error(f"Element not found with locator: {locator} and locatorType: {locator_type}")
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
        except:
            logger.error(f"Elements not found with locator: {locator} and locatorType: {locator_type}")
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
        except:
            logger.info(f"Cannot send data to element with locator: {locator} and locatorType: {locator_type}")

