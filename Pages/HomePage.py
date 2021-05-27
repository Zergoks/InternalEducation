import allure
import loguru

from Pages.BasePage import BasePage


class HomePage(BasePage):
    DynamicIdLink = ('(//h3/a)[1]', 'xpath')
    ClassAttributeLink = ('(//h3/a)[2]', 'xpath')
    HiddenLayersLink = ('(//h3/a)[3]', 'xpath')
    LoadDelayLink = ('(//h3/a)[4]', 'xpath')
    AJAXDataLink = ('(//h3/a)[5]', 'xpath')
    ClientSideDelayLink = ('(//h3/a)[6]', 'xpath')
    ClickLink = ('(//h3/a)[7]', 'xpath')
    TextInputLink = ('(//h3/a)[8]', 'xpath')
    ScrollbarsLink = ('(//h3/a)[9]', 'xpath')
    DynamicTableLink = ('(//h3/a)[10]', 'xpath')
    VerifyTextLink = ('(//h3/a)[11]', 'xpath')
    ProgressBarLink = ('(//h3/a)[12]', 'xpath')
    VisibilityLink = ('(//h3/a)[13]', 'xpath')
    SampleAppLink = ('(//h3/a)[14]', 'xpath')
    MouseOverLink = ('(//h3/a)[15]', 'xpath')
    NonBreakingSpaceLink = ('(//h3/a)[16]', 'xpath')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/home'
        self.title = 'UI Test Automation Playground'

    @allure.step("Переходим на страницу dynamic id")
    def go_to_dynamic_id_page(self):
        self.click_on_element(*self.DynamicIdLink)

    @allure.step("Переходим на страницу Class Attribute")
    def go_to_class_attribute_page(self):
        self.click_on_element(*self.ClassAttributeLink)

    @allure.step("Переходим на страницу Hidden Layers")
    def go_to_hidden_layer_page(self):
        self.click_on_element(*self.HiddenLayersLink)

    @allure.step("Переходим на страницу Load Delay")
    def go_to_load_delay_page(self):
        self.click_on_element(*self.LoadDelayLink)

    @allure.step("Переходим на страницу AJAX Data")
    def go_to_ajax_data_page(self):
        self.click_on_element(*self.AJAXDataLink)

    @allure.step("Переходим на страницу Client Side Delay")
    def go_to_client_side_delay_page(self):
        self.click_on_element(*self.ClientSideDelayLink)

    @allure.step("Переходим на страницу Click Link")
    def go_to_click_link_page(self):
        self.click_on_element(*self.ClickLink)

    @allure.step("Переходим на страницу Text Input")
    def go_to_text_input_page(self):
        self.click_on_element(*self.TextInputLink)

    @allure.step("Переходим на страницу Scroll Bars")
    def go_to_scroll_bars_page(self):
        self.click_on_element(*self.ScrollbarsLink)

    @allure.step("Переходим на страницу Dynamic Table")
    def go_to_dynamic_table_page(self):
        self.click_on_element(*self.DynamicTableLink)

    @allure.step("Переходим на страницу Verify Text")
    def go_to_verify_text_link_page(self):
        self.click_on_element(*self.VerifyTextLink)

    @allure.step("Переходим на страницу Progress Bar")
    def go_to_progress_bar_page(self):
        self.click_on_element(*self.ProgressBarLink)

    @allure.step("Переходим на страницу Visibility")
    def go_to_visibility_page(self):
        self.click_on_element(*self.VisibilityLink)

    @allure.step("Переходим на страницу Sample App")
    def go_to_sample_app_page(self):
        self.click_on_element(*self.SampleAppLink)

    @allure.step("Переходим на страницу Mouse Over")
    def go_to_mouse_over_page(self):
        self.click_on_element(*self.MouseOverLink)

    @allure.step("Переходим на страницу Non Breaking Space")
    def go_to_non_breaking_space_page(self):
        self.click_on_element(*self.NonBreakingSpaceLink)