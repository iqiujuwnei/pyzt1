import json
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testcookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    # def test_get_cookie(self):
    #     sleep(10)
    #     cookie = self.driver.get_cookies()  #有两个get_cookies 其中一个要求多传一个name
    #     with open('cookie.json', 'w') as f: #加r可读的话必须先有文件
    #         json.dump(cookie, f)
    def test_add_cookie(self):
        with open('cookie.json', 'r') as f:
            cookies = json.load(f)
            print(cookies)
        for i in cookies:
            print(i)
            self.driver.add_cookie(i)
        # sleep(5)
        # self.driver.refresh()
        #循环刷新，显式等到页面'我的企业'元素可见的时候跳出循环刷新成功
        while True:
            self.driver.refresh()
            asert = WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[@id="menu_profile"]')))
            #开始endtime是5秒总是超时，后来直接定义20秒通过了
            print(asert)
            if asert is not None:
                break
        '''
        通过定位通讯了在进行导入
        '''
        #定位到'通讯录'后点击
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]').click()
        #显式等待判断是否可见'批量导入'元素
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="ww_operationBar"]/div[2]')))
        #点击'批量导入'
        self.driver.find_element(By.XPATH, '//*[@class="ww_operationBar"]/div[2]').click()
        #显式等待判断时候否可见'导入文件'元素
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="ww_btnWithMenu js_btnWithMenu js_import_other_wrap ww_btnWithMenu_Open"]//ul//li[1]')))
        #点击'导入文件'
        self.driver.find_element(By.XPATH, '//*[@class="ww_btnWithMenu js_btnWithMenu js_import_other_wrap ww_btnWithMenu_Open"]//ul//li[1]').click()
        #显式等待'填写通讯录模版后导入'元素出现
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="js_go_template_import"]')))
        #点击'上传文件'上传自己本地文件
        self.driver.find_element(By.ID, 'js_upload_file_input').send_keys("/Users/zhangtao/PycharmProjects/pyzt1/qywx0102/zttest.xls")
        #显示等待上传'文件名'是否可见
        WebDriverWait(self.driver, 50).until(expected_conditions.presence_of_element_located((By.ID, 'upload_file_name')))
        #判断是否上传成功，核对文件名是否正确
        ast = self.driver.find_element(By.ID, 'upload_file_name').text
        assert ast == 'zttest.xls'

