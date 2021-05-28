import allure

from Pages.BasePage import BasePage
import loguru


class AJAXDataPage(BasePage):
    TriggeringAJAXButton = ('//button[@id="ajaxButton"]', 'xpath')
    SuccessNotification = ('//*[@class="bg-success"]', 'xpath')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/ajax'
        self.title = 'AJAX Data'

    @allure.step("Нажимаем на Triggering AJAX button")
    def click_on_triggering_ajax_button(self):
        self.click_on_element(*self.TriggeringAJAXButton)

