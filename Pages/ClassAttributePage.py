import allure
import loguru
from selenium.webdriver.common.by import By

from Core.ui_text import ClassAttributePage as Text
from Pages.BasePage import BasePage


class ClassAttributePage(BasePage):
    BlueButton = (".btn-primary", By.CSS_SELECTOR)
    GreenButton = (".btn-success", By.CSS_SELECTOR)
    OrangeButton = (".btn-warning", By.CSS_SELECTOR)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "/classattr"
        self.title = "Class Attribute"
        self.text = Text

    @allure.step("Нажимаем на blue button")
    def click_on_blue_button(self):
        self.click_on_element(self.BlueButton)

    def get_alert_text(self):
        elem = self.driver.switch_to.alert
        return elem.text
