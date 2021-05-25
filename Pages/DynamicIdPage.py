from Pages.BasePage import BasePage


class DynamicIdPage(BasePage):
    ButtonWithDynamicIdByXpath = ("//h4/following-sibling::button", 'xpath')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'

    def dynamic_button_is_clickable(self):
        return self.wait_for_element_to_be_clickable(*self.ButtonWithDynamicIdByXpath)