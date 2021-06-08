from time import sleep

import allure
import pytest

from Pages.HomePage import HomePage
from Pages.HiddenLayersPage import HiddenLayerPage

from Core.utils import explicit_sleep as sleep


class TestHiddenLayersPage:

    # TDD is_displayed() показывает, что зеленая кнопка есть после нажатия на неё. скрыто в доме следующим уровнем

    @allure.title("Зеленая кнопка после первого нажатия не видна на UI")
    # @pytest.mark.test
    def test_blue_button_is_not_visible_after_click(self, driver):
        home_page = HomePage(driver)
        hidden_layer_page = HiddenLayerPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_hidden_layer_page()
        sleep(1)
        hidden_layer_page.click_on_green_button()
        with allure.step("Проверям, что зеленая кнопка после нажатия не видна на UI"):
            assert hidden_layer_page.is_element_visible(hidden_layer_page.greenButton) is True, 'Visible'
