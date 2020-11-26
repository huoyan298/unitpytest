# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import os
import base64
import pyautogui
# from .AttributeManager import AttributeManager
from selenium import webdriver

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(BASE_DIR,"screenshot")

class ScreenshotCapturer():
 def __init__(self,driver=None,screenshot_dir=None):
     """配置浏览器和截图存放目录"""
     self.driver = driver
     self.set_screenshot_dir(screenshot_dir)

 def set_screenshot_dir(self,path=None):
     if path:
         path = os.path.abspath(path)
         self._create_directory(path)
     self.screenshot_root_directory = path
     return self

 def _pil_screenshot(self,file_full_path):
     img = pyautogui.screenshot()
     try:
         img.save(file_full_path,"png")
     except ValueError as ve:
         return False
     except IOError as ioe:
         return  False
     finally:
         del img
     return  True

 def _browser_screenshot(self,file_full_path):
     try:
         return self.driver.get_screenshot_as_file(file_full_path)
     except Exception:
         return False

 def screenshot(self,filename:object)->object:
     """浏览器截图失败则启动屏幕截图，返回结果和截图文件路径"""
     result = False
     path = self._get_screenshot_path(filename)
     self._create_directory(path)
     if self.driver:
        result = self._browser_screenshot(path)
     if not result:
         result = self._pil_screenshot(path)
     return (result,path)

 @classmethod
 def screenshot_file_to_base64(cls,file_full_path):
     """转为base64编码数据 """
     raw_data = ""
     try:
         with open(file_full_path,"rb") as f:
             raw_data = f.read()
     except IOError as err:
         print(err)
     return  base64.b64encode(raw_data)


 def _get_screenshot_path(self,filename):
     directory = self.screenshot_root_directory or self.SCREENSHOTS_DIR
     filename = filename.replace('/',os.sep)
     path     = os.path.join(directory,filename)
     return path

 def _create_directory(self,path):
     target_dir = os.path.dirname(path)
     if not os.path.exists(target_dir):
         os.makedirs(target_dir)


if __name__ =="__main__":
    driver = webdriver.Firefox()
    url ="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E9%BE%99%E7%8C%AB&fenlei=256&rsv_pq=8696685f0047f901&rsv_t=917a8h%2FuMoLR8EW497TiqDHXLFCqIvUuZkQZhGkshOMCk2u1Tai86t%2FKWjI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=9&rsv_sug1=1&rsv_sug7=001&rsv_sug2=0&rsv_btype=i&inputT=7780&rsv_sug4=7780&rsv_sug=9"
    driver.get(url)
    ScreenshotCapturer(driver,screenshot_dir=SCREENSHOT_DIR).screenshot("龙猫.png")

