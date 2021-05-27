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