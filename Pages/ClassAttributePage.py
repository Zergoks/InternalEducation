import allure

from Pages.BasePage import BasePage
from Core.ui_text import ClassAttributePage as Text
import loguru


class ClassAttributePage(BasePage):
    BlueButton = (".btn-primary", "css")
    GreenButton = (".btn-success", "css")
    OrangeButton = (".btn-warning", "css")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/classattr'
        self.title = 'Class Attribute'
        self.text = Text

    @allure.step("Нажимаем на blue button")
    def click_on_blue_button(self):
        self.click_on_element(*self.BlueButton)

    def get_alert_text(self):
        elem = self.driver.switch_to.alert
        return elem.text