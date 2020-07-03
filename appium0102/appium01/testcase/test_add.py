import yaml

from appium0102.appium01.base.app import App
import pytest


class TestAdd:

    def test_add(self):
        '''
        添加用户的用例
        断言是toast的添加成功
        :return:
        '''
        aet = App().start().main().goto_team().team().add_team().input_user()
        assert aet == '添加成功'