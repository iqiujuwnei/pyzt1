from appium0102.appium01.base.addteams import AddTeam
from appium0102.appium01.base.base_page import BasePage
from appium0102.appium01.base.peisoninfo import PersonInfo
from appium.webdriver.common.mobileby import MobileBy
import pytest


class Team(BasePage):

    def team(self):
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().'
                                                        'text("添加成员...").instance(0));').click()
        return AddTeam(self._driver)


    def tapuser(self):
        b = self.steps("../base/ztapp.yaml")
        uname = b['name']
        # print(type(uname))
        # print(uname)
        self._driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                                                         f'scrollable(true).instance(0)).'
                                                         f'scrollIntoView(new UiSelector().text("{uname}").instance(0));').click()
        return PersonInfo(self._driver)




