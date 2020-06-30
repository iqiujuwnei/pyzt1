from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:  # 定义公共类

    _base_url = ""  # 先定义基础的URL先为空，以遍后续不同地址调用的时候初始化

    def __init__(self, driver: WebDriver = None):  # 定义父类，调用内置的WebDriver。标识符类型识别WebDriver.初始值为None.
        self._driver = ""  # 先初始化
        if driver is None:  # 如果driver是None那么就重新分配新的driver服务。---一般测试的时候都是从长的链路。那么不能每次都要新建服务。
            option = Options()
            # 使用Google\ Chrome - -remote - debugging - port = 9222
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver  # 如果不是None 那么就沿用本身的服务
        if self._base_url != "":  # 判断ip地址，如果不是空的时候那么就初始化新的URL
            self._driver.get(self._base_url)

        self._driver.implicitly_wait(5)

    def find(self, by, locator):  # 重写find_elenmet。封装
        return self._driver.find_element(by, locator)

    def finds(self, by, enement):  # 封装find_elements
        return self._driver.find_elements(by, enement)

    def alertt(self):  # 封装alert方法
        self._driver.switch_to.alert.accept()

    def rufsh(self):  # 封装刷新方法
        self._driver.refresh()

    def quit(self):  # 封装退出
        return self._driver.quit()

    def wbewait(self, seconds, by, enemlent):
        WebDriverWait(self._driver, seconds).until(expected_conditions.presence_of_element_located((by, enemlent)))

