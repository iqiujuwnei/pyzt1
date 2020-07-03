from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.base_page import BasePage

class ToaLUser(BasePage):


    def toaluser(self):
        '''
        会员列表信息，用来校验用户删除后是否成功
        定位到已离职的元素
        :return:
        '''
        c = self.steps("../base/ztapp.yaml")
        uname = c['name']
        user_tag = self._driver.find_elements(MobileBy.XPATH, f"//*[@text='{uname}']/../../android.widget.ImageView")
        # print(self._driver.page_source)
        list01 = []
        # user_list = self._driver.find_elements(MobileBy.XPATH, "//*[@text='张涛']/../../../../../..//android.widget.TextView")
        # for i in user_list:
        #     list01.append(i.get_attribute("text"))
        # return list01
        return user_tag