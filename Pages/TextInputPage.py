import allure
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class TextInput(BasePage):
    TextInputField = ('//input[@type="text"]', By.XPATH)
    UpdatingButton = ('//button[@id="updatingButton"]', By.XPATH)

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/click'
        self.title = 'Click'

    @allure.step("Нажимаем на Updating button")
    def click_on_updating_button(self):
        self.click_on_element(*self.UpdatingButton)

    @allure.step("Вводим текст в поле для задания нового имени кнопке")
    def input_text_in_text_field(self, text):
        self.send_keys_to(text, *self.TextInputField)