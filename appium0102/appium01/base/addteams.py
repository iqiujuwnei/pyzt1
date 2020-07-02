from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.teamIput import TeamIput


class AddTeam(BasePage):

    def add_team(self):

        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return TeamIput(self._driver)