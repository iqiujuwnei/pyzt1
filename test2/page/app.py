import os

from appium import webdriver

from test2.page.base_page import BasePage
from test2.page.main import Main


class App(BasePage):


    def start(self):

        if self._driver is None:
            des_conf = {
              "platformName": "android",
              "deviceName": "emulator-5554",
              "appPackage": "com.xueqiu.android",
              "appActivity": ".view.WelcomeActivityAlias",
              "udid": os.getenv('udid', None)
                # "noReset": True
            }
            #本地机器跑脚本
            # self._driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", des_conf)
            #调用远程hub服务去分发测试脚本，使用selenium grid.
            self._driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", des_conf)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity("com.xueqiu.android", ".view.WelcomeActivityAlias")
        return self  #调用自己

    def main(self):
        return Main(self._driver)