from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.base_page import BasePage
from appium0102.appium01.base.team import Team


class Main(BasePage):

    def goto_team(self):
        '''
        在首页进入团队列表页面
        :return:
        '''
        self.find_clck(MobileBy.XPATH, "//*[@text='团队']")

        # self.find(MobileBy.XPATH, "//*[@class='android.widget.TextView']")
        # self.find(MobileBy.XPATH, "//*[@text='团队']").click()
        return Team(self._driver)
