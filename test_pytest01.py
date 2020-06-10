import pytest
import yaml


class Test_cacle:
    with open('pyzt.yml', 'rb') as f:
        data = yaml.safe_load(f)

    @pytest.mark.parametrize(['a', 'b'], data)
    def test_add(self, a, b):
        sum_c = a + b
        print(f"{a}+{b}={sum_c}")
        return sum_c

    @pytest.mark.parametrize(['a', 'b'], data)
    def test_subtract(self, a, b):
        subtract_s = a - b
        print(f"{a}-{b}={subtract_s}")
        return subtract_s

    @pytest.mark.parametrize(['a', 'b'], data)
    def test_multiply(self, a, b):
        multiply_m = a * b
        print(f"{a}*{b}={multiply_m}")
        return multiply_m

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
    pytest.main(['test_pytest01.py', '-vs'])
