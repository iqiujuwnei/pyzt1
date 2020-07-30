import requests
from hamcrest import *
class TestWechatAccess:
    # 实例化会话对象
    s = requests.Session()
    def setup(self):
        params={
            "corpid":"ww44051ca7a74ae8e3",
            "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        # 将token放入会话对象中
        self .s.params.update({"access_token": res.json()['access_token']})

    # 添加成员
    def test_addMember(self):
        data = {
                "userid": "zhangsan",
                "name": "张三",
                "mobile": "13800000009",
                "department": [1]
        }

        res = self.s.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create',json=data)
        # 将userid放入会话对象中
        self.s.params.update({"userid": "zhangsan"})
        # assert(self.test_getMember()['name']=="张三")
        print(res.json())