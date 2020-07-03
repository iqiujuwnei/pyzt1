import yaml
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:
    _params = []

    def __init__(self, driver: WebDriver = None):
        '''
        base数据，调用driver服务
        :param driver:
        '''
        self._driver = driver

    def find(self, by, locator=None):
        '''
        封装find_element方法
        :param by:
        :param locator:
        :return:
        '''
        return self._driver.find_element(by, locator)

    def steps(self, path):
        '''
        封装打开数据方法
        :param path:
        :return:
        '''
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            print(steps)
        for step in steps:
            return step

