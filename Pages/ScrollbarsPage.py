import allure
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ScrollbarsPage(BasePage):
    HidingButton = ('//*[@id="hidingButton"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/scrollbars"
        self.title = "Scrollbars"

    @allure.step("Нажимаем на Hiding button")
    def click_on_hiding_button(self):
        self.click_on_element(self.HidingButton)

    @allure.step("Скролим страницу к Hiding button")
    def scroll_to_hiding_button(self):
        self.scroll_into_view(self.HidingButton)
