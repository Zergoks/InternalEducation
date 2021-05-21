import loguru

from Core.driver_custom import DriverCustom
from Core.ui_map import home_page


class HomePage(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/home'
        self.title = 'UI Test Automation Playground'

    def go_to_dynamic_id_page(self):
        element_locator = (home_page['DynamicIdLinkByXpath'], 'xpath')
        self.wait_for_element_to_be_clickable(*element_locator)
        self.click_on_element(home_page['DynamicIdLinkByXpath'], 'xpath')
