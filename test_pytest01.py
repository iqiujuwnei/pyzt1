import pytest
import yaml
import allure

@allure.feature("计算机测试集")
class Test_cacle:
    with open('pyzt.yml', 'rb') as f:
        data = yaml.safe_load(f)
        print(data)
    @allure.story("加法测试")
    @pytest.mark.parametrize(['a', 'b'], data)
    def test_add(self, a, b):
        sum_c = a + b
        print(f"{a}+{b}={sum_c}")
        return sum_c
    @allure.story("减法测试")
    @allure.severity(allure.severity_level.TRIVIAL)
    @pytest.mark.add1
    @pytest.mark.parametrize(['a', 'b'], data)
    def test_subtract(self, a, b):
        subtract_s = a - b
        print(f"{a}-{b}={subtract_s}")
        return subtract_s
    @allure.story("乘法测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('http//:www.baidu.com', name="通用链接")  #通用链接方法
    @allure.testcase("http://www.baidu.com", name="测试用例")  #测试用例链接
    # --allure-link-pattren=issue:http://www.baidu.com/issue/{}
    @allure.issue('140', name='BUG地址链接')  #BUG地址链接
    @pytest.mark.add2
    @pytest.mark.parametrize(['a', 'b'], data)
    def test_multiply(self, a, b):
        with allure.step('参数作乘法运算'):
            multiply_m = a * b
        print(f"{a}*{b}={multiply_m}")
        with allure.step('返回相乘的数据'):
            return multiply_m
    @allure.story("除法测试")
    # @allure.attach('文本', attachment_type=allure.attachment_type.TEXT)
    # @allure.attach('<body>html</body>', attachment_type=allure.attachment_type.HTML)
    # @allure.attach.file('图片地址', name="这是图片", attachment_type=allure.attachment_type.JPG)
    @pytest.mark.skip
    @pytest.mark.parametrize(['a', 'b'], data)
    def test_divide(self, a, b):
        if b == 0:
            print("分母不能为0")
            raise Exception
        else:
            divide_d = a / b
            print(f"{a}/{b}={divide_d}")
            return divide_d


if __name__ == '__main__':
    pytest.main(['test_pytest01.py', '--setup-show'])
