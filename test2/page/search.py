from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from test2.page.base_page import BasePage


class Search(BasePage):

    def goto_result(self):
        #his.locatorStrategies = ['xpath', 'id', 'class name', 'accessibility id', '-android uiautomator'];
        #by 的几种方式，虽然写的时候是MobileBy.I。但是实际使用的id所以ymal文件by 的值只能是id
        self.setps("../page/serach.yaml")