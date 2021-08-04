import allure
import pytest

from Pages.HomePage import HomePage
from Pages.VisibilityPage import VisibilityPage


@allure.suite("Visibility Page UI")
class TestVisibilityPage:

    @allure.title("После нажатия на Hide Button кнопка Removed скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_removed_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Removed Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.RemovedButton) is True, \
                "Removed Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step("Проверям, что Removed Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.RemovedButton) is False, \
                "Removed Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Zero Width Button скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_zero_width_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Zero Width Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.ZeroWidthButton) is True, \
                "Zero Width Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step("Проверям, что Zero Width Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.ZeroWidthButton) is False, \
                "Zero Width Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Overlapped Button  скрывается на UI ")
    @pytest.mark.xfail(reason="Тест падает т.к. элемент фактически \"Перекрывается\" "
                       "другим элементом и для селениума все еще видим")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_overlapped_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Overlapped Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.OverlappedButton) is True, \
                "Overlapped Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step("Проверям, что Overlapped Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.OverlappedButton) is False, \
                "Overlapped Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Zero Opacity Button  скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_zero_opacity_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Zero Opacity Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.ZeroOpacityButton) is True, \
                "Zero Opacity Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step("Проверям, что Zero Opacity Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.ZeroOpacityButton) is False, \
                "Zero Opacity Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Visibility Hidden Button  скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_visibility_hidden_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Visibility Hidden Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.VisibilityHiddenButton) is True, \
                "Visibility Hidden Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step(
                "Проверям, что Visibility Hidden Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.VisibilityHiddenButton) is False, \
                "Visibility Hidden Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Display None Button скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_display_none_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Display None Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.DisplayNoneButton) is True, \
                "Display None Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step(
                "Проверям, что Display None Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.DisplayNoneButton) is False, \
                "Display None Button отображается после нажатия на Hide Button"

    @allure.title("После нажатия на Hide Button кнопка Off Screen Button скрывается на UI ")
    @pytest.mark.test
    def test_check_after_pressing_hide_button_display_off_screen_button_is_not_visible(self, driver):
        home_page = HomePage(driver)
        visibility_page = VisibilityPage(driver)
        home_page.go_to_home_page()
        home_page.go_to_visibility_page()
        with allure.step("Проверям, что Off Screen Button отображается на странице после загрузки"):
            assert visibility_page.is_element_visible(visibility_page.OffScreenButton) is True, \
                "Off Screen Button не отображается после загрузки страницы"
        visibility_page.click_on_hide_button()
        with allure.step(
                "Проверям, что Off Screen Button не отображается на странице после нажатия на Hide Button"):
            assert visibility_page.is_element_visible(visibility_page.OffScreenButton) is False, \
                "Off Screen Button отображается после нажатия на Hide Button"
