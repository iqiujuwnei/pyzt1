import pytest
import yaml

from appium0102.appium01.base.app import App

with open("../base/ztapp.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    data_ad = datas['ad']
    data_de = datas['de']

class TestDel:

    @pytest.mark.parametrize('name, phone, genders', data_de)
    def test_del(self, name, phone, genders):
        '''
        删除用户的用例
        断言的方式是删除后定位到已离职。表示是否存在这个元素
        :return:
        '''
        a = App().start().main().goto_team().tapuser(name).personinfo().setuser().edituser().toaluser(name)
        assert a
