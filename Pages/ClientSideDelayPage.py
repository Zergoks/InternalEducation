import allure
import pytest
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ClientSideDelay(BasePage):
    TriggeringClientSideLogicButton = ('//button[@id="ajaxButton"]', By.XPATH)
    SuccessNotification = ('//*[@class="bg-success"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/clientdelay'
        self.title = 'Client Side Delay'

    @allure.step("Нажимаем на Triggering Client Side Logic button")
    def click_on_triggering_client_side_logic_button(self):
        self.click_on_element(self.TriggeringClientSideLogicButton)
