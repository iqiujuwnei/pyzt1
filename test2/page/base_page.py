import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

class BasePage:

    _toast_list = [(MobileBy.ID, 'image_cancel')]
    _error_cont = 0
    _error_max = 10

    def __init__(self, driver: WebDriver=None):
        self._driver = driver
    # 查找的时候会有弹屏处理，将弹屏关闭才能进行下一步点击
    def find(self, by, locator=None):
        try:
            elem = self._driver.find_element(by, locator)
            self._error_cont = 0  #不能一直try下去，必须有个计数点。
            return elem
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._toast_list:
                ele = self._driver.find_elements(*black) #看看是否找到了本来定义的弹屏数据。
                if len(ele) > 0:  #找到后可定是有数据的
                    ele[0].click()  #找到后就点击关闭
                    return self.find(by, locator) #关闭后再次返回查找定位的元素
            raise e
    #弹屏不一定再找的时候弹出，有可能是我们已经找到。点击输入的时候弹出。这个时候需要再输入的时候做弹屏处理
    def send(self, vaule, by, locator=None):
        try:
            ele1 = self.find(by, locator).send_keys(vaule)
            self._error_cont = 0
            return ele1
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._toast_list:
                ele = self._driver.find_elements(*black)
                if len(ele) > 0:
                    ele[0].click()
                    return self.send(vaule, by, locator)
            raise e


    def setps(self, path):
        with open(path, encoding="utf-8") as f:   #数据处理，利用yaml.因为测试数据是多个。所以我们要做的是循环找出

            setps: list[dict] = yaml.safe_load(f)
            print(setps)

        for step in setps:
            if "by" in step.keys():
                elenmt = self.find(step['by'], step['locator'])
            if 'action' in step.keys():
                if step["action"] == 'click':
                    elenmt.click()
                if step['action'] == 'send':
                    self.send(step['value'], step['by'], step['locator'])

