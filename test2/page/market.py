from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from test2.page.base_page import BasePage
from test2.page.search import Search


class Market(BasePage):

    def goto_search(self):
        self.find(MobileBy.ID, "action_search").click()
        return Search(self._driver)