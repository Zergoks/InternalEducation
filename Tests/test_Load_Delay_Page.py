import allure
import pytest

from Pages.HomePage import HomePage
from Pages.LoadDelayPage import LoadDelayPage


@allure.suite("Load Delay Page UI")
class TestLoadDelayPage:

    @allure.title("Синяя кнопка кликабельна после длительной загрузки страницы")
    def test_blue_button_is_clickable_after_delay(self, driver):
        home_page = HomePage(driver)
        load_delay_page = LoadDelayPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_load_delay_page()
        with allure.step("Проверяем, что синяя кнопка кликабельна"):
            assert load_delay_page.is_element_clickable(*load_delay_page.AppearingAfterDelayButton) is True, \
                "Не кликабельна синяя кнопка кнопка"
