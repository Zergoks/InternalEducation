import allure
import pytest

from Pages.HomePage import HomePage
from Pages.ClientSideDelayPage import ClientSideDelay

from Core.utils import explicit_sleep as sleep


@allure.suite("AJAX Data Page UI")
class TestClientSideDelayPage:

    @allure.title("После успешного выполнения логики на стороне пользователя появляется нотификация")
    def test_client_logic_success_notification_is_visible(self, driver):
        home_page = HomePage(driver)
        client_delay_page = ClientSideDelay(driver)
        home_page.go_to_home_page()
        home_page.go_to_client_side_delay_page()
        sleep(1)
        client_delay_page.click_on_triggering_client_side_logic_button()
        with allure.step("Проверям, что за 30 секунд появляется нотификация успехом запроса"):
            assert client_delay_page.is_element_visible(client_delay_page.SuccessNotification, timeout=30) is True, \
                "Не появилась нотификация"
