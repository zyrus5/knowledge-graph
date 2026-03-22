import pytest


@pytest.fixture
def f1():
    print('前置操作_f1')
    yield
    print('后置操作_f1')
    pass


class TestFixture:
    def test_1(self, f1):
        """
        使用fixture方式一：参数列表
        """
        pass

    @pytest.mark.usefixtures("f1")
    def test_2(self):
        """
        使用fixture方式二：使用标记
        """
        pass


@pytest.fixture(autouse=True)
def f2_auto_use():
    print('前置操作_f2')
    yield
    print('后置操作_f2')
    pass


class TestFixtureAutoUse:
    def test_1(self):
        pass

    def test_2(self):
        pass


@pytest.fixture
def f3_quote(f1):
    print('前置操作_f3')
    yield
    print('后置操作_f3')
    pass


class TestFixtureQuote:

    @pytest.mark.usefixtures("f3_quote")
    def test_1(self):
        pass


@pytest.fixture
def f4_return():
    print('前置操作_f4')
    yield 1, 2.0, "3"
    print('后置操作_f4')
    pass


class TestFixtureReturn:

    def test_1(self, f4_return):
        print(f'接收到fixture的返回值: type={type(f4_return)}, value={f4_return}')
        pass


class TestFixtureShare:

    def test_1(self, f_session_return):
        print(f'接收到session fixture的返回值: type={type(f_session_return)}, value={f_session_return}')
        pass
