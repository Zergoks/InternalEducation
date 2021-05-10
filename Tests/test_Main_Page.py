from Pages.HomePage import HomePage


class TestMainPage:

    def test_dynamic_id_link_is_present(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_page()
        assert home_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                f'EX: {home_page.title}, ' \
                                                f'AR: {driver.title}'
