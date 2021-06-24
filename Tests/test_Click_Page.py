import allure
import pytest

from Core.utils import explicit_sleep as sleep
from Pages.ClickPage import ClickPage
from Pages.HomePage import HomePage


@allure.suite("Click Page UI")
class TestClickPage:
    @allure.title("После нажатия bad button изменяется на success button")
    def test_success_button_is_visible_after_click_bad_button(self, driver):
        home_page = HomePage(driver)
        click_page = ClickPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_click_page()
        sleep(1)
        click_page.click_on_bad_button()
        with allure.step(
            "Проверям, что после нажатия на bad button появился success button",
        ):
            assert (
                click_page.is_element_clickable(click_page.SuccessButton) is True
            ), "Не появилась success button"
        with allure.step(
            "Проверям, что bad button больше не кликабельна после нажатия",
        ):
            assert (
                click_page.is_element_clickable(click_page.BadButton) is False
            ), "Bad button кликабельна"
