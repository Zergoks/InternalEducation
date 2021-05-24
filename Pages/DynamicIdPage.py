from Pages.BasePage import BasePage


class DynamicIdPageLocators:
    ButtonWithDynamicIdByXpath = "//h4/following-sibling::button"


class DynamicIdPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'
