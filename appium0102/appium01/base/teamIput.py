
from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
import pytest
import yaml


class TeamIput(BasePage):

    def input_user(self, name, phone, genders):
        '''
        个人编辑页面输入用户必填数据
        调用yaml数据必填项：姓名，性别，手机号
        :return:
        '''
        # a = self.steps("../base/ztapp.yaml")
        gender = genders
        self.find_send(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText", name)
        self.find_clck(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
        if gender == "女":
            self.find_clck(MobileBy.XPATH, "//*[@text='女']")
        else:
            self.find_clck(MobileBy.XPATH, "//*[@text='女']/../../../..//*[@text='男']")
        self.find_send(MobileBy.XPATH, "//*[@text='手机号']", phone)
        self.find_clck(MobileBy.XPATH, "//*[@text='保存']")
        #toast定位的方式，Android的固定写法。取出text值然后返给用例
        testtoast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return testtoast

