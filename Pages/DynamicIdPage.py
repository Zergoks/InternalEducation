import allure

from Pages.BasePage import BasePage


class DynamicIdPage(BasePage):
    ButtonWithDynamicIdByXpath = ("//h4/following-sibling::button", 'xpath')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'

    def dynamic_id_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(*self.ButtonWithDynamicIdByXpath)

    @allure.step("Получаем значение аттрибута у dynamic_id_button")
    def get_attribute_of_dynamic_id_button(self, attribute) -> str:
        value = self.get_element_attribute(attribute, *self.ButtonWithDynamicIdByXpath)
        allure.attach(body=value, name=attribute)
        return value
