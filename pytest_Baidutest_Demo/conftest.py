# encoding:utf-8


"""
@author:@huoyanyang
@note:fixture
"""
from selenium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.support.wait import WebDriverWait
import time
@pytest.fixture(scope ='module')
def pytest_addoption(parser):
    parser.addini('nice', type = 'bool', default = True, help= '添加 ini参数')

def get_ini(pytestconfig):
     nice = pytestconfig.getini('nice')
     print(nice)

@pytest.fixture
def login_baidu():
    dr = webdriver.Firefox()
    dr.get('http://www.baidu.com')
    dr.maximize_window()
    time.sleep(4)
    WebDriverWait(dr, 2).until(lambda x: x.find_element_by_xpath('//*[@id="u1"]/a[8]').is_displayed())
    #WebDriverWait(dr,2).until(lambda x: x.find_element_by_xpath(''))
    #dr.find_element(By.XPATH, '//*[@id="u1"]/a[7]').click()
    dr.find_element( By.XPATH, '//*[@id="u1"]/a[8]' ).click()
    "判断默认展示的是扫码登录还是用户名登录"

    try:

         WebDriverWait(dr, 2).until(lambda x: x.find_element_by_xpath('//p[@title="用户名登录"][not@style)]').is_displayed())
        #dr.find_element( By.ID, "TANGRAM__PSP_10__footerULoginBtn" ).click()
         b = 1
    except:
        #b = 2
         b = 1
         print("exception")
         #moren登录方式未扫码
    if b == 1:
        dr.find_element("xpath", '//p[@title="用户名登录"]').click()
        dr.find_element(By.NAME, "userName").send_keys('115566957@qq.com')
        dr.find_element(By.NAME, "password").send_keys('*******')
        #dr.find_element(By.ID, "TANGRAM_PSP_10_submit").click()
        dr.find_element( By.XPATH, '//*[@id="TANGRAM__PSP_10__submit"]' ).click()
        time.sleep(10)
        print('one')
        yield dr
        dr.quit()
        #def quit():
        #    print('run')
        #    dr.quit()
        #request.addfinalizer(quit)




