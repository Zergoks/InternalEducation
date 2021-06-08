import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DynamicIdPage(BasePage):
    ButtonWithDynamicId = ("//h4/following-sibling::button", By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'

    @allure.step("Получаем значение аттрибута у dynamic_id_button")
    def get_attribute_of_dynamic_id_button(self, attribute) -> str:
        value = self.get_element_attribute(attribute, self.ButtonWithDynamicId)
        allure.attach(body=value, name=attribute)
        return value
