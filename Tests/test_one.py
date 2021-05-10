from Pages.MainPage import MainPage

class TestMainPage:
    def test_succ(self, driver):
        driver.get('https://demoqa.com/')
        main_page = MainPage(driver)
        elem = main_page.get_element('img213312')
        assert elem in '12323231'