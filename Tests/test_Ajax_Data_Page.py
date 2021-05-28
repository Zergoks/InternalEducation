import allure
import pytest

from Pages.HomePage import HomePage
from Pages.AJAXDataPage import AJAXDataPage

from Core.utils import explicit_sleep as sleep


@allure.suite("AJAX Data Page UI")
class TestAJAXDataPage:

    @allure.title("После успешного выполнения ajax запроса появляется нотификация")
    def test_ajax_success_notification_is_visible(self, driver):
        home_page = HomePage(driver)
        ajax_data_page = AJAXDataPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_ajax_data_page()
        sleep(1)
        ajax_data_page.click_on_triggering_ajax_button()
        with allure.step("Проверям, что в течение 30 появляется нотификация успехом запроса"):
            assert ajax_data_page.is_element_visible(*ajax_data_page.SuccessNotification, timeout=30) is True, \
                "Не появилась нотификация"
