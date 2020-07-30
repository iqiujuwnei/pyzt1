from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from test2.page.base_page import BasePage
from test2.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find(MobileBy.XPATH, "//*[@resource-id='android:id/tabhost']//*[@text='行情']").click()
        return Market(self._driver)
