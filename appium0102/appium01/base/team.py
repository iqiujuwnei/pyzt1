from appium0102.appium01.base.addteams import AddTeam
from appium0102.appium01.base.base_page import BasePage
from appium0102.appium01.base.peisoninfo import PersonInfo
from appium.webdriver.common.mobileby import MobileBy
import pytest


class Team(BasePage):

    def team(self):
        '''
        在团队列表页面点击添加成员
        因为这个页面是因为人员数据的增加自动增加的，进入的时候当前页面可能看不到添加成员按钮
        所以需要采用滑动查找元素的方式
        :return:
        '''
        self._driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).'
                                                        'instance(0)).scrollIntoView(new UiSelector().'
                                                        'text("添加成员...").instance(0));').click()
        return AddTeam(self._driver)


    def tapuser(self,name):
        '''
        滑动查找用户名字
        :return:
        '''
        # b = self.steps("../base/ztapp.yaml")
        # uname = b['name']
        # print(type(uname))
        # print(uname)
        self._driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().'
                                                         f'scrollable(true).instance(0)).'
                                                         f'scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        return PersonInfo(self._driver)




