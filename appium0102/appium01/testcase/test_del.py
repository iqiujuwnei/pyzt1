from appium0102.appium01.base.app import App


class TestDel:

    def test_del(self):
        '''
        删除用户的用例
        断言的方式是删除后定位到已离职。表示是否存在这个元素
        :return:
        '''
        a = App().start().main().goto_team().tapuser().personinfo().setuser().edituser().toaluser()
        assert a
