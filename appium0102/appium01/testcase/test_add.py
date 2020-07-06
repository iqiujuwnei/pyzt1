import yaml

from appium0102.appium01.base.app import App
import pytest

with open("../base/ztapp.yaml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    data_ad = datas['ad']
    data_de = datas['de']

class TestAdd():

    @pytest.mark.parametrize('name, phone, genders', data_ad)
    def test_add(self, name, genders, phone):
        '''
        添加用户的用例
        断言是toast的添加成功
        :return:
        '''
        aet = App().start().main().goto_team().team().add_team().input_user(name, genders, phone)
        assert aet == '添加成功'
        # App().back()
