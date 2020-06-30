from selenium.webdriver.common.by import By
from qywx0102.page.adduser import AddUser
from qywx0102.page.base_page import BasePage
from qywx0102.page.deluser import DelUser
from qywx0102.page.importuser import ImportUser
from qywx0102.page.maillist import MailList


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def goto_add(self):
        self.find(By.CSS_SELECTOR, '.ww_operationBar .js_add_member').click()
        return AddUser(self._driver)

    def goto_deluser(self):
        return DelUser(self._driver)

    def goto_maillist(self):
        return MailList(self._driver)

    def goto_import_user(self):
        return ImportUser(self._driver)
