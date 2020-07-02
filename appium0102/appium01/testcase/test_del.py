from appium0102.appium01.base.app import App


class TestDel:

    def test_del(self):
        a = App().start().main().goto_team().tapuser().personinfo().setuser().edituser().toaluser()
        assert a
