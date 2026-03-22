import allure
import pytest


@allure.epic('goodnight')
@allure.feature('登录')
@allure.story('登录')
@allure.title('登录-成功')
def test_01():
    assert True


@allure.epic('goodnight')
@allure.feature('登录')
@allure.story('登录')
@allure.title('登录-用户名密码错误')
@pytest.mark.xfail
def test_02():
    assert False


@allure.epic('goodnight')
@allure.feature('用户管理')
@allure.story('新增用户')
@allure.title('全信息修改')
def test_03():
    assert True
