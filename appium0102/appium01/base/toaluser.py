from appium.webdriver.common.mobileby import MobileBy

from appium0102.appium01.base.base_page import BasePage

class ToaLUser(BasePage):


    def toaluser(self, name):
        '''
        会员列表信息，用来校验用户删除后是否成功
        定位到已离职的元素
        WebDriverWait(self.driver, 15).until_not(lambda x:x.find_element_by_xpath(f"//*[@text='{username}']"))
        :return:
        '''
        # c = self.steps("../base/ztapp.yaml")
        # uname = c['name']
        #删除的时候我这企业微信的版本会一直显示已离职状态不会消失
        #user_tag = self.webwait_not(10, MobileBy.XPATH, f"//*[@text='{uname}']")

        #定位到删除用户的名称，然后找到已离职的标签。就算删除成功。
        user_tag = self.find(MobileBy.XPATH, f"//*[@text='{name}']/../../android.widget.ImageView")

        return user_tag