from selenium.webdriver.common.by import By
from qywx0102.page.base_page import BasePage
from qywx0102.page.maillist import MailList


class DelUser(BasePage):
    def del_user(self):
        self.find(By.CSS_SELECTOR, '.js_ww_table>.ui-sortable:nth-last-child(2)').click()  # 每次新增都在倒数第二个，所以删除新增的不影响其他人数据
        self.find(By.CSS_SELECTOR, '.js_del_member').click()
        self.find(By.LINK_TEXT, "确认").click()
        self.rufsh()
        return MailList(self._driver)
