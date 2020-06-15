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
        self.driver.implicitly_wait()
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
