import allure

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class DynamicTablePage(BasePage):
    DynamicTable = ('//div[@role="table"]', By.XPATH)
    ContentOfDynamicTable = ('//div[@role="rowgroup"][2]', By.XPATH)
    HeadersInDynamicTable = ('//span[@role="columnheader"]', By.XPATH)
    RowWithDataInDynamicTable =('//div[@role="rowgroup"][2]/div[@role="row"]', By.XPATH)
    NamesOfRowsInDynamicTable = ('//div[@role="row"]/span[@role="cell"][1]'), By.XPATH
    LineWithExpectedResult = ('//p[@class="bg-warning"]', By.XPATH)


    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamictable'
        self.title = 'Dynamic Table'

    # @allure.step("Получаем значение аттрибута у dynamic_id_button")
    # def get_attribute_of_dynamic_id_button(self, attribute) -> str:
    #     value = self.get_element_attribute(attribute, self.ButtonWithDynamicId)
    #     allure.attach(body=value, name=attribute)
    #     return value

    @allure.step('Получаем ожидаемый результат из Желтого лейбла')
    def get_expected_result(self):
        return self.get_element_text(self.LineWithExpectedResult)

    def __get_index_of_wanted_column(self, expected_result):
        headers = self.get_elements(self.HeadersInDynamicTable)
        header_names = [x.text for x in headers]
        wanted_header = expected_result[1]
        return header_names.index(wanted_header) if wanted_header in header_names else False

    def __get_index_of_wanted_row(self, expected_result):
        names = self.get_elements(self.NamesOfRowsInDynamicTable)
        names = [name.text for name in names]
        wanted_name = expected_result[0]
        return names.index(wanted_name) if wanted_name in names else False

    def get_value_from_table_by_expected_result(self, expected_result):
        expected_result = [x.rstrip(':') for x in expected_result.split(' ')]
        wanted_row = self.__get_index_of_wanted_row(expected_result) + 1
        wanted_column = self.__get_index_of_wanted_column(expected_result) + 1
        wanted_element = (f'{self.ContentOfDynamicTable[0]}/div[{wanted_row}]/span[{wanted_column}]', By.XPATH)
        return self.get_element_text(wanted_element)
