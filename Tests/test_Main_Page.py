import allure
import pytest
from Pages.HomePage import HomePage


@pytest.mark.test
class TestMainPage:
    def test_home_page_title_is_correct(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_home_page()
        assert home_page.at_page() is True, f'Не на странице home_page.' \
                                            f'EX: home page' \
                                            f'AR: {driver.current_url}'
        with allure.step("Сравниваем текущий тайтл страницы с ожидаемым"):
            assert home_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                    f'EX: {home_page.title}, ' \
                                                    f'AR: {driver.title}'
