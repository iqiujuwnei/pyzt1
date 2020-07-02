from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
# class TestApp:
#     def setup(self):
#
#         self.des_conf = {
#           "platformName": "android",
#           "deviceName": "emulator-5554",
#           "appPackage": "com.xueqiu.android",
#           "appActivity": ".view.WelcomeActivityAlias",
#             "noReset": True
#         }
#     def test_app(self):
#         self.driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", self.des_conf)
#         self.driver.implicitly_wait(15)
#         el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
#         el1.click()
#         el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
#         el2.send_keys("阿里巴巴")
#         el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
#         el3.click()
        #
        # action = TouchAction(self.driver)
        # action.press()

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
des_conf = {
  "platformName": "android",
  "deviceName": "emulator-5554",
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
}
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", des_conf)
driver.implicitly_wait(15)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("阿里巴巴")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el3.click()