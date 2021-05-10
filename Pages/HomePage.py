from Core.driver_custom import DriverCustom
from Core.ui_map import home_page


class HomePage(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/home'
        self.title = 'ToolsQA'
