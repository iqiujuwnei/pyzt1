from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testfuyong:
    def test_fuyong(self):
        option = Options()
        # 使用Google\ Chrome - -remote - debugging - port = 9222
        option.debugger_address = "localhost:9222"
        driver = webdriver.Chrome(options=option)
        #先手动登陆一次然后再次访问
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        #使用中很多不遍，1、反应很慢，2、Firefox的使用不方便，3、google 浏览器常用经常会所以不小心就忘记关闭