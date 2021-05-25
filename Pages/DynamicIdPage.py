from Pages.BasePage import BasePage


class DynamicIdPageLocators:
    ButtonWithDynamicIdByXpath = ("//h4/following-sibling::button", 'xpath')


class DynamicIdPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'

    def dynamic_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(*DynamicIdPageLocators.ButtonWithDynamicIdByXpath)