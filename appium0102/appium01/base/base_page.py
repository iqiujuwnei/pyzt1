import yaml
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    def find_clck(self, by, locator=None):
        '''
        封装点击方法
        '''
        self.find(by, locator).click()
    def find_send(self,by, locator=None, element=None):
        '''
        封装输入方法
        '''
        self.find(by, locator).send_keys(element)

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

    def wbewait(self, seconds, by, enemlent):
        WebDriverWait(self._driver, seconds).until(expected_conditions.presence_of_element_located((by, enemlent)))

    def webwait_not(self, seecods, by, loact ):
        WebDriverWait(self._driver, seecods).until_not(lambda x: x.find_element(by, loact))

    def back(self, num=1):
        self.back(num)
