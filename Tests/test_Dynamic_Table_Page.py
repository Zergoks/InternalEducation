import allure
import pytest

from Pages.HomePage import HomePage
from Pages.DynamicTablePage import DynamicTablePage


@allure.suite("Dynamic Table Page UI")
class TestDynamicTablePage:

    @allure.title("Значение в соответствующей ячейки таблицы совпадает с "
                  "ожидаемым результатом написанным в желтом лейбле")
    def test_cpu_from_expected_result_match_value_in_table(self, driver):
        home_page = HomePage(driver)
        dynamic_table_page = DynamicTablePage(driver)
        home_page.go_to_home_page()
        home_page.go_to_dynamic_table_page()
        expected_result = dynamic_table_page.get_expected_result()
        expected_result_cpu = expected_result.split(' ')[2]
        with allure.step("Проверям, что полученый ожидаемый результат совпадает с значеним в таблице"):
            assert expected_result_cpu == dynamic_table_page.get_value_from_table_by_expected_result(expected_result)
