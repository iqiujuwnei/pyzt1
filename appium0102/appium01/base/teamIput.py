
from appium0102.appium01.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy
import pytest
import yaml


class TeamIput(BasePage):

    def input_user(self):
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
        testtoast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return testtoast

