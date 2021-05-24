import allure
from loguru import logger
from Core.driver_custom import DriverCustom


class HeaderLocators:
    UITAPLink = ("//a[@class='navbar-brand']", 'xpath')
    HomePageLink = ("//a[@href='/home']", 'xpath')
    ResourcesPageLink = ("//a[@href='/resources']", 'xpath')


class Header(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_ui_tap(self):
        with allure.step("Переходим по лого в хедере"):
            self.click_on_element(*HeaderLocators.UITAPLink)

    def go_to_home_page(self):
        with allure.step("Переходим по Home в хедере"):
            self.click_on_element(*HeaderLocators.HomePageLink)

    def go_to_resources_page(self):
        with allure.step("Переходим по Resources в хедере"):
            self.click_on_element(*HeaderLocators.ResourcesPageLink)


class BasePage(DriverCustom):

    def __init__(self, driver, has_header=True):
        super().__init__(driver)
        self.base_url = 'http://uitestingplayground.com'
        self.url = '/'

        if has_header:
            self.header = Header(driver)

    def go_to_home_page(self):
        logger.info(f"go to {self.base_url}")
        with allure.step("Переходим на main page"):
            self.driver.get(self.base_url+self.url)