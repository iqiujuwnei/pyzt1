from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from qywx0102.page.base_page import BasePage
from qywx0102.page.maillist import MailList


class ImportUser(BasePage):

    def import_user(self):
        self.find(By.XPATH, '//*[@id="menu_contacts"]').click()
        # 显式等待判断是否可见'批量导入'元素
        self.wbewait(10, By.XPATH, '//*[@class="ww_operationBar"]/div[2]')
        # WebDriverWait(self.driver, 10).until(
        #     expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="ww_operationBar"]/div[2]')))
        # 点击'批量导入'
        self.find(By.XPATH, '//*[@class="ww_operationBar"]/div[2]').click()
        # 显式等待判断时候否可见'导入文件'元素
        self.wbewait(10, By.XPATH,
                     '//*[@class="ww_btnWithMenu js_btnWithMenu js_import_other_wrap ww_btnWithMenu_Open"]//ul//li[1]')
        # 点击'导入文件'
        self.find(By.XPATH,
                  '//*[@class="ww_btnWithMenu js_btnWithMenu js_import_other_wrap ww_btnWithMenu_Open"]//ul//li[1]').click()
        # 显式等待'返回'元素出现
        self.wbewait(20, By.CSS_SELECTOR, '#import_back_no_loading')
        # 点击'上传文件'上传自己本地文件
        self.find(By.ID, 'js_upload_file_input').send_keys("/Users/zhangtao/Downloads/importzt.xls")
        sleep(50)
        # 显式等待上传'文件名'是否可见
        # self.wbewait(50, By.ID, 'upload_file_name')
        #点击去导入
        self.find(By.CSS_SELECTOR, '#submit_csv').click()
        # 显式等待去查看按钮是否可见
        self.wbewait(30, By.CSS_SELECTOR, '#reloadContact')
        self.find(By.CSS_SELECTOR, '#reloadContact').click()
        # 显式等待添加会员按钮是否可见
        self.wbewait(10, By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        return MailList
