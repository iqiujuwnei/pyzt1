from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.teamIput import TeamIput


class AddTeam(BasePage):

    def add_team(self):
        '''
        用户列表页面，手动添加
        :return:
        '''

        self.find_clck(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return TeamIput(self._driver)