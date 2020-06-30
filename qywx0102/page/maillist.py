from selenium.webdriver.common.by import By
from qywx0102.page.base_page import BasePage


class MailList(BasePage):

    def getuser(self):
        userlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list_usr = [i.get_attribute("title") for i in userlist]
        # for i in userlist:
        #     list_usr.append(i.get_attribute("title"))
        return list_usr  # 获取列表后查看用户是否在列表中
