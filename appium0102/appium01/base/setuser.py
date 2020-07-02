from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.edituser import EditUser


class SetUser(BasePage):

    def setuser(self):

        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditUser(self._driver)