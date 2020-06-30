from qywx0102.page.main import Main


class Test_Import:
    def setup(self):
        self.main = Main()

    def test_import(self):
        assert "test17" in self.main.goto_import_user().import_user().getuser()

