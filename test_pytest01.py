import pytest
import yaml
import allure

@allure.feature("计算机测试集")
class Test_cacle:
    with open('pyzt.yml', 'rb') as f:
        data = yaml.safe_load(f)
        print(data)

    @pytest.mark.run(order=2)       #更改排序为第二
    @pytest.mark.dependency(depends=["adda"]) #执行依赖加法
    @allure.story("减法测试")       # allure story方法
    @allure.severity(allure.severity_level.TRIVIAL)     # allure 级别不重要  默认是normal
    @pytest.mark.add1       #增加的执行标签
    @pytest.mark.parametrize(['a', 'b', 'subtract'], data['sub'])  #参数化数据
    def check_subtract(self, a, b, subtract):     #更改了执行规则check_* 和 test_*
        assert subtract == a - b


    @pytest.mark.run(order=1)       #更改排序为第一
    @pytest.mark.dependency(name="adda")        #被依赖
    @allure.story("加法测试")       # allure story方法
    @pytest.mark.parametrize(['a', 'b', 'sum_c'], data['add'])      #参数化数据
    def test_add(self, a, b, sum_c):
        assert sum_c == a + b
        print(f"{a}+{b}={sum_c}")
        return sum_c

    @pytest.mark.dependency(name="multiply")
    @allure.story("乘法测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link('http//:www.baidu.com', name="通用链接")  #通用链接方法
    @allure.testcase("http://www.baidu.com", name="测试用例")  #测试用例链接
    # --allure-link-pattren=issue:http://www.baidu.com/issue/{}
    @allure.issue('140', name='BUG地址链接')  #BUG地址链接
    @pytest.mark.add2
    @pytest.mark.parametrize(['a', 'b', 'multiply'], data['mult'])
    def test_multiply(self, a, b, multiply):
        with allure.step('参数作乘法运算'):
            multiply == a * b
        with allure.step('返回相乘的数据'):
            return multiply

    @pytest.mark.dependency(depends=["multiply"])
    @allure.story("除法测试")
    # @allure.attach('文本', attachment_type=allure.attachment_type.TEXT)
    # @allure.attach('<body>html</body>', attachment_type=allure.attachment_type.HTML)
    # @allure.attach.file('图片地址', name="这是图片", attachment_type=allure.attachment_type.JPG)
    #@pytest.mark.skip
    @pytest.mark.parametrize(['a', 'b', 'divide'], data['dive'])
    def test_divide(self, a, b, divide):
        if b == 0:
            print("分母不能为0")
            raise Exception
        else:
            assert divide == a / b



if __name__ == '__main__':
    pytest.main(['test_pytest01.py', '--setup-show'])
