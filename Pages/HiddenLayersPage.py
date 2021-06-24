import allure
import pytest
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HiddenLayerPage(BasePage):
    greenButton = ('//*[@id="greenButton"]', By.XPATH)
    blueButton = ('//*[@id="blueButton"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/hiddenlayers"
        self.title = "Hidden Layers"

    @allure.step("Нажимаем на зеленую кнопку")
    def click_on_green_button(self):
        self.click_on_element(self.greenButton)

    @allure.step("Нажимаем на синюю кнопку")
    def click_on_blue_button(self):
        self.click_on_element(self.blueButton)
