import pytest
from Pages.HomePage import HomePage
from Core.ui_map import home_page as ui_home_page


class TestMainPage:
    @pytest.mark.test
    def test_dynamic_id_link_is_present(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_page()
        home_page.scroll_into_view(ui_home_page['DynamicIdLinkByCSS'])
        assert home_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                f'EX: {home_page.title}, ' \
                                                f'AR: {driver.title}'
