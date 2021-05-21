from Core.driver_custom import DriverCustom


class HeaderLocators:
    UITAPLink = ('', '')
    HomePageLink = ('', '')
    ResourcesPageLink = ('', '')


class Header(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_ui_tap(self):
        self.click_on_element(*HeaderLocators.UITAPLink)

    def go_to_home_page(self):
        self.click_on_element(*HeaderLocators.HomePageLink)

    def go_to_resources_page(self):
        self.click_on_element(*HeaderLocators.ResourcesPageLink)


class BasePage(DriverCustom):

    def __init__(self, driver, has_header=True):
        super().__init__(driver)
        if has_header:
            self.header = Header(driver)
