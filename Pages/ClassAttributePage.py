from Pages.BasePage import BasePage
import loguru


class ClassAttributePage(BasePage):
    BlueButton = (".btn-primary", "css")
    GreenButton = (".btn-success", "css")
    OrangeButton = (".btn-warning", "css")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/classattr'
        self.title = 'Class Attribute'

    def button_is_clickable(self, button):
        return self.wait_for_element_to_be_clickable(*button)
