import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ClickPage(BasePage):
    BadButton = ('//*[@class="btn btn-primary"]', By.XPATH)
    SuccessButton = ('//*[@class="btn btn-success"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/click'
        self.title = 'Click'

    @allure.step("Нажимаем на Bad button")
    def click_on_bad_button(self):
        self.click_on_element(self.BadButton)
