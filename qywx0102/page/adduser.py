from time import sleep
from selenium.webdriver.common.by import By
from qywx0102.page.base_page import BasePage
from qywx0102.page.maillist import MailList


class AddUser(BasePage):
    def add_user(self):
        self.find(By.ID, "username").send_keys("test7")
        self.find(By.ID, "memberAdd_acctid").send_keys("026")
        self.find(By.ID, "memberAdd_phone").send_keys("13511189999")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        sleep(5)
        return MailList(self._driver)
