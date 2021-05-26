import allure
from loguru import logger
from Core.driver_custom import DriverCustom


class Header(DriverCustom):
    UITAPLink = ("//a[@class='navbar-brand']", 'xpath')
    HomePageLink = ("//a[@href='/home']", 'xpath')
    ResourcesPageLink = ("//a[@href='/resources']", 'xpath')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переходим по лого в хедере")
    def click_on_uitap(self):
        self.click_on_element(*self.UITAPLink)

    @allure.step("Переходим по Home в хедере")
    def go_to_home_page(self):
        self.click_on_element(*self.HomePageLink)

    @allure.step("Переходим по Resources в хедере")
    def go_to_resources_page(self):
        self.click_on_element(*self.ResourcesPageLink)

    def at_page(self):
        return True if self.get_element('body>nav', 'css') else False



class BasePage(DriverCustom):

    def __init__(self, driver, has_header=True):
        super().__init__(driver)
        self.base_url = 'http://uitestingplayground.com'
        self.url = '/'

        if has_header:
            self.header = Header(driver)

    @allure.step("Переходим на main page")
    def go_to_home_page(self):
        logger.info(f"go to {self.base_url}")
        self.driver.get(self.base_url + self.url)

    def at_page(self) -> bool:
        return self.base_url + self.url == self.driver.current_url

    @allure.step("Обновляем страницу")
    def refresh_page(self):
        logger.info(f"refresh page")
        self.driver.refresh()

    @allure.step("Подтверждаем alert")
    def accept_alert(self):
        self.switch_to_alert().accept()