import allure
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoadDelayPage(BasePage):
    AppearingAfterDelayButton = ('//*[@class="container"]/button', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/loaddelay'
        self.title = 'Load Delays'

    @allure.step("Нажимаем на blue button")
    def click_on_appearing_after_delay_button(self):
        self.click_on_element(*self.AppearingAfterDelayButton)