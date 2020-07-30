import sys
sys.path.append('/Users/zhangtao/PycharmProjects/pyzt1')
from test2.page.app import App


class TestSearch:

    def test_search(self):
        App().start().main().goto_market().goto_search().goto_result()