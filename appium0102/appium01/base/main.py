from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.base_page import BasePage
from appium0102.appium01.base.team import Team


class Main(BasePage):

    def goto_team(self):
        self._driver.find_element(MobileBy.XPATH, "//*[@text='团队']").click()

        # self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView']")
        # self.find(MobileBy.XPATH, "//*[@text='团队']").click()
        return Team(self._driver)
