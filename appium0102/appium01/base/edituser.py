from time import sleep

from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


from appium0102.appium01.base.toaluser import ToaLUser


class EditUser(BasePage):

    def edituser(self):

        self.find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        sleep(5)#页面反应迟钝，加了强制等待。后续优化为显式等待

        return ToaLUser(self._driver)