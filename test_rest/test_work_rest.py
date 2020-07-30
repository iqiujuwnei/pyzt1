import pytest
import requests
import yaml


class TestRest:
    with open('/Users/zhangtao/PycharmProjects/pyzt1/test_rest/work.yml', 'rb') as f:
        datas = yaml.safe_load(f)
        print(datas)
        print(datas['add'])

    def test_get_token(self):
        params = {
              "corpid": "wwba36badfb10abc79",
              "corpsecret": "P05mVM5qvKDoCu2hpqivgkrezhv7X7PyAc5o_lgMyk0"
        }
        result = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        # print(result.text)
        print(result.json()["access_token"])
        global token
        token = result.json()["access_token"]
        try:
            return token
        except Exception as e:
            raise ValueError("token is invalid")
    @pytest.mark.parametrize(('userid','name','mobile'), datas['add'])
    def test_user_create(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }

        result1 = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}", json=data)
        print(result1.json())

    new_list = []
    for i in datas['add']:
        new_list.append(i[0])
        # print(new_list)
    # @pytest.mark.parametrize('a', datas['add']) 直接传带userID的列表也能通过
    @pytest.mark.parametrize('userid', new_list)
    def test_user_read(self, userid):
        data = {
            "access_token": token,
            "userid": userid
        }
        result2 = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get", params=data)
        print(result2.json())

    @pytest.mark.parametrize(('userid', 'name', 'mobile'), datas['update'])
    def test_user_update(self, userid, name, mobile):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1]
        }
        result3 = requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=data)
        print(result3.json())
    @pytest.mark.parametrize('userid', new_list)
    def test_user_delete(self, userid):
        data = {
            "access_token": token,
            "userid": userid
        }
        result4 = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=data)
        print(result4.json())