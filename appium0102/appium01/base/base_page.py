import yaml
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:
    _params = []

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, by, locator=None):
        return self._driver.find_element(by, locator)

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps: list[dict] = yaml.safe_load(f)
            print(steps)
        for step in steps:
            return step

