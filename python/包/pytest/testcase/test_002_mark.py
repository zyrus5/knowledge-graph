import pytest
import csv


def add(a, b):
    return a + b


class TestCustom:

    @pytest.mark.api_s
    def test_int(self):
        assert add(1, 2) == 3

    @pytest.mark.api_c
    def test_str(self):
        assert str(add('1', '2')) == "3"

    @pytest.mark.web
    def test_list(self):
        assert add([1], [2, 3]) == [1, 2, 3]


def load_data(path):
    fd = open(path)
    reader = csv.reader(fd)
    return list(reader)[1:]


class TestBuiltin:

    @pytest.mark.skip
    def test_skip(self):
        assert add(1, 2) == 4

    @pytest.mark.skipif(1 == 1, reason='自定义跳过原因')
    def test_skip(self):
        assert add(1, 2) == 4

    @pytest.mark.xfail
    def test_xfail_pass(self):
        assert add(1, 2) == 4

    @pytest.mark.xfail
    def test_xfail_x_pass(self):
        assert add(1, 2) == 3

    @pytest.mark.parametrize('a, b, c', load_data('asserts/mark_parametrize_data.csv'))
    def test_parametrize(self, a, b, c):
        """
        数据驱动测试
        """
        assert add(int(a), int(b)) == int(c)
