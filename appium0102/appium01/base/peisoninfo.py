from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.setuser import SetUser


class PersonInfo(BasePage):

    def personinfo(self):

        self.find(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//android.widget.RelativeLayout").click()

        return SetUser(self._driver)