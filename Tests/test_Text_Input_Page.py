import allure
import pytest

from Pages.HomePage import HomePage
from Pages.TextInputPage import TextInput

from Core.utils import explicit_sleep as sleep


@allure.suite("Text Input Page UI")
class TestTextInputPage:

    @allure.title("После заполнения текстового поля и нажатия кнопки изменяется название кнопки")
    @pytest.mark.test
    def test_button_name_is_changed_after_click(self, driver):
        home_page = HomePage(driver)
        text_input_page = TextInput(driver)
        home_page.go_to_home_page()
        home_page.go_to_text_input_page()
        sleep(1)
        text_input_page.send_keys_to('qawe', *text_input_page.TextInputField)
        text_input_page.click_on_updating_button()
        with allure.step("Проверям, что после нажатия название кнопки изменилось на ввреденное в текстовое поле"):
            assert text_input_page.get_element(*text_input_page.UpdatingButton).text == 'qawe', \
                "Текст кнопки не равен введенному значению в поле"