import pytest


@pytest.fixture(scope='session', autouse=True)
def f_session():
    """

    :return:
    """
    print('session级别前置操作')
    yield
    print('session级别后置操作')
    pass


@pytest.fixture(scope='session', autouse=True)
def f_session_return():
    """

    :return:
    """
    print('session级别前置操作')
    yield "session_return"
    print('session级别后置操作')
    pass
