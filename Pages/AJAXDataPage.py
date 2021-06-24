import allure
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class AJAXDataPage(BasePage):
    TriggeringAJAXButton = ('//button[@id="ajaxButton"]', By.XPATH)
    SuccessNotification = ('//*[@class="bg-success"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/ajax"
        self.title = "AJAX Data"

    @allure.step("Нажимаем на Triggering AJAX button")
    def click_on_triggering_ajax_button(self):
        self.click_on_element(self.TriggeringAJAXButton)
