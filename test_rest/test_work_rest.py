import pytest
import requests
import yaml
from hamcrest import *


class TestRest:
    with open('/Users/zhangtao/PycharmProjects/pyzt1/test_rest/work.yml', 'rb') as f:
        datas = yaml.safe_load(f)
        # print(datas)
        # print(datas['add'])
    s = requests.Session() #调用session方法，跨请求保持数据
    def setup(self):
        params = {
            "corpid": "wwba36badfb10abc79",
            "corpsecret": "P05mVM5qvKDoCu2hpqivgkrezhv7X7PyAc5o_lgMyk0"
        }
        result = self.s.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # result = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # print(result.text)
        # print(result.json()["access_token"])
        '''
        不使用Session。通过传递token的方式来进行接口测试
        global token  设置全局变量省的大很多字- 、-
        token = result.json()["access_token"]
        try:
            return token
        except Exception as e:
            raise ValueError("token is invalid")
        '''

        self.s.params.update({"access_token": result.json()["access_token"]}) #将数据参数更新保存token。跨请求的时候直接带入


    @pytest.mark.parametrize(('userid', 'name', 'mobile'), datas['add'])
    def test_user_create(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        result1 = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        # print(result1.json())
        '''
        通过传递的方式拿取token
        result1 = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}", json=data)
        '''

        assert_that(0, equal_to(result1.json()['errcode']))

    #单独获取userID，接口其实可以直接用必填数据
    new_list = []
    for i in datas['add']:
        new_list.append(i[0])
        # print(new_list)

    # @pytest.mark.parametrize('a', datas['add']) 直接传带userID的列表也能通过
    @pytest.mark.parametrize('userid', new_list)
    def test_user_read(self, userid):
        data = {
            # "access_token": token,
            "userid": userid
        }
        result2 = self.s.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=data)
        '''
        通过传递的方式拿取token
        result2 = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=data)
        '''

        assert_that('ok', equal_to(result2.json()['errmsg']))
        # print(result2.json())

    @pytest.mark.parametrize(('userid', 'name', 'mobile'), datas['update'])
    def test_user_update(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        result3 = self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        '''
        通过传递的方式拿取token
        result3 = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=data)
        '''

        assert_that(0, equal_to(result3.json()['errcode']))

        # print(result3.json())

    @pytest.mark.parametrize('userid', new_list)
    def test_user_delete(self, userid):
        data = {
            # "access_token": token,
            "userid": userid
        }
        result4 = self.s.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=data)
        '''
        通过传递的方式拿取token
        result4 = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=data)
        '''

        assert_that('deleted', equal_to(result4.json()['errmsg']))
        # print(result4.json())
