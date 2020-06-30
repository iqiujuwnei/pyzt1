
from qywx0102.page.main import Main


class TestDel:
    def setup(self):
        self.main = Main()

    def test_deluser(self):
        # assert "test7" in self.main.goto_add().add_user().getuser()
        self.main.goto_deluser().del_user().getuser()
        # assert "test7" not in self.main.goto_deluser().del_user().getuser()
