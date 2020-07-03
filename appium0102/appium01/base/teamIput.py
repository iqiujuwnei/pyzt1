
from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
import pytest
import yaml


class TeamIput(BasePage):

    def input_user(self):
        '''
        个人编辑页面输入用户必填数据
        调用yaml数据必填项：姓名，性别，手机号
        :return:
        '''
        a = self.steps("../base/ztapp.yaml")
        gender = a['gender']
        self.find(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(a['name'])
        self.find(MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']").click()
        if gender == "女":
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']/../../../..//*[@text='男']").click()
        self.find(MobileBy.XPATH, "//*[@text='手机号']").send_keys(a['phone'])
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        #toast定位的方式，Android的固定写法。取出text值然后返给用例
        testtoast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return testtoast

