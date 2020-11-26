#encoding:utf-8
"""
author:huoyan
"""
import pytest
from selenium.webdriver.remote.webdriver import By
from selenium.webdriver.common.keys import Keys
from Pytest_Baidutest_Demo import pri_packaging
import time
#from Pytest_Baidutest_Demo.conftest import login_baidu

class Test_baidu():
    def test_search(self, login_baidu):
        """
        :param login_baidu:搜索
        :return:
        """
        dr = login_baidu
        #dr.find_element(By.ID, "kw").send_keys('aaa', Keys.ENTER)
        dr.find_element( By.XPATH, '//*[@id="kw"]' ).send_keys('aaa',Keys.ENTER)

    def test_setting(self, login_baidu):
        """
        :param login_baidu:
        :return:
        """
        dr = login_baidu
        """
       dr.find_element(By.XPATH, '//*[@id= "s_usersetting_top"]/span').click()
       #点击设置
       dr.find_element(By.XPATH,'//*[@id= "wrapper"]/div[5]/a[1]').click()
       #搜索设置
       pri_packaging.wait_element_appear(dr,value= '//*[@id= "s1_2"]')
       dr.find_element(By.XPATH, '//*[@id="s1_2"]').click()
       #搜索框提示不显示
       """
        dr.find_element(By.XPATH, '//*[@id= "u"]/a[3]').click()
        dr.find_element(By.XPATH, '//*[@id="wrapper"]/div[4]/a[1]').click()
        pri_packaging.wait_element_appear( dr, value='//*[@id= "s1_2"]' )
        dr.find_element( By.XPATH, '//*[@id="s1_2"]' ).click()
        time.sleep(5)

if __name__ == '__main__':
    pytest.main(["-s","test_baidu.py"])
