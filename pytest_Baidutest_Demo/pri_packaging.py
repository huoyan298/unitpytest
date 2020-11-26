# encoding:utf-8
"""
author:huoyan
pycharm 封装常用的方法
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import By

def wait_element_appear(driver,timeout= 10,by= By.XPATH,value=None ):
     WebDriverWait(driver, timeout, 1).until(lambda x: x.find_element(by,value).is_displayed())