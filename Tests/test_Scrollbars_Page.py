import allure
import pytest

from Pages.ScrollbarsPage import ScrollbarsPage
from Pages.HomePage import HomePage

from Core.utils import sleep


@allure.suite("Scrollbars Page UI")
class TestMainPage:

    @allure.title("У Main page корректный title")
    @pytest.mark.test
    def test_home_page_title_is_correct(self, driver):
        home_page = HomePage(driver)
        scrollbars_page = ScrollbarsPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_scroll_bars_page()
        scrollbars_page.scroll_to_hiding_button()
        with allure.step("Проверяем, что кнопка видна после скролла к кнопке"):
            assert scrollbars_page.is_element_visible(scrollbars_page.HidingButton) is True, \
                "Кнопка не видна после скролла"
        with allure.step("Проверяем, что кнопка кликабельна после скролла к кнопке"):
            assert scrollbars_page.is_element_clickable(scrollbars_page.HidingButton) is True, \
                "На кнопку нельзя нажать"
