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

    @pytest.mark.test
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
