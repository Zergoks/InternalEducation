import pytest
from Pages.HomePage import HomePage


class TestMainPage:
    @pytest.mark.test
    def test_dynamic_id_link_is_present(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_page()
        home_page.get_element('#overview>.container>.row:nth-of-type(1)>.col-sm:nth-of-type(1)')
        assert home_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                f'EX: {home_page.title}, ' \
                                                f'AR: {driver.title}'
