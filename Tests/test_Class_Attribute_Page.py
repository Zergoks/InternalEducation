import allure
import pytest

from Pages.HomePage import HomePage
from Pages.ClassAttributePage import ClassAttributePage


class TestClassAttributePage:

    @allure.title("У dynamic id page корректный title")
    def test_dynamic_id_page_title_is_correct(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        with allure.step("Сравниваем текущий тайтл страницы с ожидаемым"):
            assert class_attribute_page.title in driver.title, f'Тайтл страницы отличается. ' \
                                                               f'EX: {class_attribute_page.title}, ' \
                                                               f'AR: {driver.title}'

    @allure.feature("Header")
    @allure.title("Header присутствует на странице Class Attribute")
    def test_header_is_present(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        with allure.step("Проверяем, что header присутствует на странице"):
            assert class_attribute_page.header.at_page() is True, f'Отсутствует header на странице'

    @allure.feature("Blue button")
    @allure.title("Blue button на странице Class Attribute кликабельна")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blue_button_is_clickable(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        with allure.step("Проверяем, что кнопка кликабельна"):
            assert class_attribute_page.button_is_clickable(ClassAttributePage.BlueButton) is True, \
                "Blue button не кликабельна"

    @allure.feature("Blue button")
    @allure.title("После нажатия на Blue button на странице Class Attribute появляется alert")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blue_button_alert(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        class_attribute_page.click_on_blue_button()
        with allure.step("Проверяем, что появился alert"):
            assert class_attribute_page.is_alert_present() is True, \
                "Alert не появился"

    @pytest.mark.test
    @allure.feature("Blue button")
    @allure.title("Алерт после нажатия кнопки содержит текст")
    @allure.severity(allure.severity_level.NORMAL)
    def test_blue_button_alert(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        class_attribute_page.click_on_blue_button()
        with allure.step("Проверяем, текст в alert соответствует требованиям"):
            assert class_attribute_page.get_alert_text() == class_attribute_page.text["BlueButtonAlertText"], \
                f"Текст alert не соответствует требованиям.\n" \
                f"AR: {class_attribute_page.get_alert_text()}\n " \
                f"EX: {class_attribute_page.text['BlueButtonAlertText']}"

    @allure.feature("Green button")
    @allure.title("Green button на странице Class Attribute кликабельна")
    @allure.severity(allure.severity_level.MINOR)
    def test_green_button_is_clickable(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        with allure.step("Проверяем, что кнопка кликабельна"):
            assert class_attribute_page.button_is_clickable(ClassAttributePage.GreenButton) is True, \
                "Green button не кликабельна"

    @allure.feature("Orange button")
    @allure.title("Orange button на странице Class Attribute кликабельна")
    @allure.severity(allure.severity_level.MINOR)
    def test_orange_button_is_clickable(self, driver):
        home_page = HomePage(driver)
        class_attribute_page = ClassAttributePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_class_attribute_page()
        with allure.step("Проверяем, что кнопка кликабельна"):
            assert class_attribute_page.button_is_clickable(ClassAttributePage.OrangeButton) is True, \
                "Orange button не кликабельна"
