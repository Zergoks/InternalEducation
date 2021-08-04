import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class VisibilityPage(BasePage):
    HideButton = ('//*[@id="hideButton"]', By.XPATH)
    RemovedButton = ('//*[@id="removedButton"]', By.XPATH)
    ZeroWidthButton = ('//*[@id="zeroWidthButton"]', By.XPATH)
    OverlappedButton = ('//*[@id="overlappedButton"]', By.XPATH)
    ZeroOpacityButton = ('//*[@id="transparentButton"]', By.XPATH)
    VisibilityHiddenButton = ('//*[@id="invisibleButton"]', By.XPATH)
    DisplayNoneButton = ('//*[@id="notdisplayedButton"]', By.XPATH)
    OffScreenButton = ('//*[@id="offscreenButton"]', By.XPATH)


    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/visibility'
        self.title = 'Visibility'

    # @allure.step("Получаем значение аттрибута у dynamic_id_button")
    # def get_attribute_of_dynamic_id_button(self, attribute) -> str:
    #     value = self.get_element_attribute(attribute, self.ButtonWithDynamicId)
    #     allure.attach(body=value, name=attribute)
    #     return value

    @allure.step("Нажимаем на Hide button")
    def click_on_hide_button(self):
        self.click_on_element(self.HideButton)

