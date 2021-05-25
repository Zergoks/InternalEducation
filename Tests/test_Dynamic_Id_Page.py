import allure
import pytest
from Pages.HomePage import HomePage
from Pages.DynamicIdPage import DynamicIdPage


class TestDynamicIdPage:
    def test_dynamic_id_page_title_is_correct(self, driver):
        home_page = HomePage(driver)
        dynamic_id_page = DynamicIdPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_dynamic_id_page()
        with allure.step("Сравниваем текущий тайтл страницы с ожидаемым"):
            assert dynamic_id_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                            f'EX: {dynamic_id_page.title}, ' \
                                                            f'AR: {driver.title}'

    # @pytest.mark.test
    def test_button_with_dynamic_id_is_clickable(self, driver):
        home_page = HomePage(driver)
        dynamic_id_page = DynamicIdPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_dynamic_id_page()
        with allure.step("Проверяем, что кнопка dynamic id кликабельна"):
            assert dynamic_id_page.dynamic_button_is_clickable() is True, f'Кнопка dynamic id не кликабельна.'

    @pytest.mark.test
    def test_header_is_present(self, driver):
        home_page = HomePage(driver)
        dynamic_id_page = DynamicIdPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_dynamic_id_page()
        with allure.step("Проверяем, что header присутствует на странице"):
            assert dynamic_id_page.header.at_page() is True, f'Отсутствует header на странице'