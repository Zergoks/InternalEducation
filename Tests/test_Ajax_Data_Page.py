import allure
import pytest

from Pages.AJAXDataPage import AJAXDataPage
from Pages.HomePage import HomePage


@allure.suite("AJAX Data Page UI")
@pytest.mark.test
class TestAJAXDataPage:
    @allure.title("После успешного выполнения ajax запроса появляется нотификация")
    @pytest.mark.smoke
    def test_ajax_success_notification_is_visible(self, driver):
        home_page = HomePage(driver)
        ajax_data_page = AJAXDataPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_ajax_data_page()
        ajax_data_page.click_on_triggering_ajax_button()
        with allure.step(
            "Проверям, что в течение 30 появляется нотификация успехом запроса",
        ):
            assert (
                ajax_data_page.is_element_visible(
                    ajax_data_page.SuccessNotification,
                    timeout=30,
                )
                is True
            ), "Не появилась нотификация"
