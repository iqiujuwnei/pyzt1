import pytest

@pytest.fixture(autouse=True,)                          #每一个函数或方法都会调用
# @pytest.fixture(autouse=True, scope='class')          #每一个类调用一次，一个类中可以有多个方法
# @pytest.fixture(autouse=True, scope='module')         #每一个.py文件调用一次，该文件内又有多个function和class
# @pytest.fixture(autouse=True, scope='session')        #是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module

def start():
    print("开始计算")
    yield
    end()


def end():
    print("计算结束")
