import pytest
from Pages.HomePage import HomePage
from Pages.DynamicIdPage import DynamicIdPage


class TestMainPage:
    @pytest.mark.test
    def test_dynamic_id_link_is_present(self, driver):
        home_page = HomePage(driver)
        dynamic_id_page = DynamicIdPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_dynamic_id_page()
        assert dynamic_id_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                      f'EX: {dynamic_id_page.title}, ' \
                                                      f'AR: {driver.title}'
