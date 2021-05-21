from Core.driver_custom import DriverCustom


class DynamicIdPageLocators:
    ButtonWithDynamicIdByXpath = "//h4/following-sibling::button"


class DynamicIdPage(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'
