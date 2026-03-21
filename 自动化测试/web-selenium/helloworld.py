from selenium import webdriver
from selenium.webdriver.common.by import By  # 引入 By 模块
from selenium.webdriver.support.wait import WebDriverWait


def demo_find_element():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    wait = WebDriverWait(driver, 10)  # 指定等待超时时间10s
    wait.until(lambda d: {
        # 这里写等待结束的逻辑
        1 == 1
    })

    driver.get("https://www.bing.com")
    el_by_id = driver.find_element(By.ID, 'sb_form_q')
    print(el_by_id)
    el_by_xpath = driver.find_element(By.XPATH, '//*[@id="sb_form_q"]')
    print(el_by_xpath)
    el_by_selector = driver.find_element(By.CSS_SELECTOR, '#sb_form_q')
    print(el_by_selector)

    driver.quit()


# 3. 标准的 Python 脚本运行入口
if __name__ == '__main__':
    print()
    demo_find_element()
