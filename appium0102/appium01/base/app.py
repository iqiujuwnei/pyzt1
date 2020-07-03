from appium.webdriver import webdriver
from appium import webdriver

from appium0102.appium01.base.base_page import BasePage
from appium0102.appium01.base.main import Main


class App(BasePage):

    def start(self):
        '''
        配置基础信息
        :return:
        '''

        if self._driver is None:
            ap_dec = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "True"
            }
            self._driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", ap_dec)
            self._driver.implicitly_wait(15)

        else:
            self._driver.start_activity('com.tencent.wework', '.launch.WwMainActivity')

        return self
    def main(self):
        '''
        调用main函数
        :return:
        '''
        return Main(self._driver)
