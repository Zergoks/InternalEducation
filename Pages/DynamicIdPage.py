from Core.driver_custom import DriverCustom


class DymamicIdPage(DriverCustom):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = '/dynamicid'
        self.title = 'Dynamic ID'