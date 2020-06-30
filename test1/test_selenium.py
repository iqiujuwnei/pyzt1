import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestBaidu():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.set_window_size(1680, 1027)
        self.driver.find_element(By.ID, "kw").click()
        self.driver.find_element(By.ID, "kw").send_keys("kaixin")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        self.driver.execute_script("window.scrollTo(0,349)")
        WebDriverWait(self.driver, 30000).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, "开心_十年之约_开心有你_今日火爆公测")))


import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestGuangbiao():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_guangbiao(self):
        self.driver.get("https://store.gaojihealth.cn/user/login")
        self.driver.set_window_size(1680, 1050)
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_handler-9MIt6")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_drag_text-3HvDN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_drag_text-3HvDN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".index_handler-9MIt6").click()


import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import al


class TestDenglu():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_denglu(self):
        self.driver.get("https://store.gaojihealth.cn/user/login")
        self.driver.set_window_size(1680, 1050)
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("18291733117")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("123qaz")
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_handler-9MIt6")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_drag_text-3HvDN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".index_drag_text-3HvDN")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.CSS_SELECTOR, ".index_handler-9MIt6").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn").click()



class Testb:
    def setup(self):
        self.dirver = webdriver.Chrome()
        self.dirver.maximize_window()
        self.dirver.implicitly_wait(5)
    def teardown(self):
        self.dirver.quit()

    def test_ka(self):
        self.dirver.get("https://www.baidu.com")
        self.dirver.find_element(By.ID, 'kw').click()
        self.dirver.find_element(By.ID, 'kw').send_keys("firefox")
        self.dirver.find_element(By.ID, 'su').click()
        time.sleep(5)
        self.dirver.back()
        time.sleep(5)
        self.dirver.find_element(By.ID, 'kw').click()
        self.dirver.find_element(By.ID, 'kw').send_keys('selenium')
        self.dirver.find_element(By.ID, 'su').click()
        time.sleep(15)
        self.dirver.find_element(By.CLASS_NAME, '')
