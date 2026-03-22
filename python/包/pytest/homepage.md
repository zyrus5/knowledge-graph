<!-- TOC -->
* [环境搭建](#环境搭建)
* [用例结果说明](#用例结果说明)
* [命令](#命令)
* [标记](#标记)
  * [自定义标记](#自定义标记)
  * [框架内置标记](#框架内置标记)
* [fixture](#fixture)
  * [高级用法](#高级用法)
* [插件](#插件)
  * [插件管理](#插件管理)
  * [常用插件](#常用插件)
* [Allure](#allure)
  * [装饰器](#装饰器)
<!-- TOC -->

# 环境搭建

* 创建python环境：`uv init --python 3.13 testcase`
* 添加依赖：`uv add --dev pytest`
* 运行测试用例：`uv run pytest`

# 用例结果说明

| 缩写 | 单词      | 含义              |
|----|---------|-----------------|
| .  | passed  | 通过              |
| F  | failed  | 失败（用例执行时报错）     |
| E  | error   | 出错（fixture执行报错） |
| s  | skipped | 跳过              |
| X  | xpassed | 预期外的通过（不符合预期）   |
| x  | xfailed | 预期内的失败（符合预期）    |

# 命令

* `-v`
  * 增加详细输出
* `-s`
  * 用例中正常使用输入输出
* `-x`
  * 快速退出

# 标记

* 执行`uv run pytest --markers`可以查看所有标记。

## 自定义标记

* 通过配置文件定义。[示例](testcase/pytest.ini)

```ini
[pytest]

markers =
    api_s: 服务端接口测试
    api_c: C端接口测试
    web: web端接口测试
```

* 然后就可以在测试用例里使用自定义标记了

```python
import pytest


@pytest.mark.web
def test_int():
    assert 1 == 3
```

* 执行`uv run pytest -m web`可以仅执行标记下的用例

## 框架内置标记

* @pytest.mark.filterwarnings(warning)
* @pytest.mark.skip(reason=None)
* @pytest.mark.skipif(condition, ..., *, reason=...)
* @pytest.mark.xfail(condition, ..., *, reason=..., run=True, raises=None, strict=strict_xfail)
* @pytest.mark.parametrize(argnames, argvalues)
  * [示例](testcase/test_002_mark.py)
* @pytest.mark.usefixtures(fixturename1, fixturename2, ...)
  * [跳转](#fixture)

# fixture

* 创建
  * 使用`yeild`关键字分割前置操作和后置操作

```python
import pytest


@pytest.fixture
def f():
    print('前置操作')
    yield
    print('后置操作')
    pass
```

* 使用
  * 方式1: [参数列表](testcase/test_003_fixture.py)
  * 方式2：[给`用例`加标记](testcase/test_003_fixture.py)

## 高级用法

* 自动使用
  * 定义fixture时指定`autouse=True`
  * 这样.py中的所有用例都会执行该fixture

```python
import pytest


@pytest.fixture(autouse=True)
def f2_share():
    print('前置操作_f2')
    yield
    print('后置操作_f2')
    pass
```

* 依赖使用
  * fixture也可以依赖fixture，只需要在fixture的参数定义中引入其他fixture即可
  * [示例](testcase/test_003_fixture.py)

* 返回内容
  * 在`yeild`关键字后可添加返回值
  * 测试用例使用参数的方式使用fixture，测试用例中接收到的就是fixture返回的值了
  * [示例](testcase/test_003_fixture.py)

* 范围共享
  * 一些初始化操作（比如启动浏览器比较耗时），可以将变量共享给其他用例
  * 通过`@pytest.fixture`的`scope`指定共享范围，scope的取值范围如下
    * function
      * 默认
    * session
      * 使用`conftest.py`定义全局的fixture
      * 注意必须设置fixture的`autouse=True`
    * package
    * module
    * class
  * [示例](testcase/test_003_fixture.py)

# 插件

## 插件管理

* 通过`-p`指定启用/禁用插件
  * 启用
    * 示例：`uv run pytest --html=report.html`
  * 禁用
    * 示例：`uv run pytest --html=report.html -p no:html`
* 插件使用方式
  * 参数方式
  * 配置文件
    * 在`pytest.ini`文件中增加`addopts = 插件参数`
    * [示例](testcase/pytest.ini)
  * fixture
  * 标记

## 常用插件

* pytest-html
  * 生成测试报告
  * 示例：`uv run pytest --html=report.html`
  * 插件已经被 [allure](#allure) 替代
* pytest-xdist
  * 分布式执行，将不同的用例分配给不同的进程执行
  * 参数：
    * `-n`: 指定进程数
  * 示例：`uv run pytest -n 3`
* pytest-rerunfailures
  * 用例失败之后重新执行
  * 参数：
    * `--reruns` 重新执行的次数
    * `--reruns-delay` 重试的间隔，单位秒
  * 示例：`uv run pytest --reruns 5 --reruns-delay 3`
* pytest-result-log
  * 将用例的执行结果记录到日志文件
  * 参数：
  * 示例：

# Allure

* allure 是目前主流的测试报告工具，支持步骤展示、用例分类、失败截图 / 日志、趋势分析，报告可交互性极强。
* allure
  * 安装：
    * macOS：`brew install allure`
  * 使用
    * 方式1: 执行`allure generate allure-results -o allure-report --clean`生成静态HTML报告
    * 方式2: 启动本地服务打开报告`allure serve allure-results`
      * 默认地址：[http://127.0.0.1:5252](http://127.0.0.1:5252)

## 装饰器

* `@allure.epic`
  * 项目
* `@allure.feature`
  * 模块
* `@allure.story`
  * 功能
* `@allure.title`
  * 用例
* [示例](testcase/test_004_allure.py)