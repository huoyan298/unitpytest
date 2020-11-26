#--encoding:utf-8

#import configobj import ConfigObj
import configparser

import os

#class LoginPage(BasePage)


class ReadConfig(object):
    """配置参数"""
    def __init__(self):
       """
        conf = ReadConfig()
        confinfo = conf.getconf("url")
        """
       #设置conf.ini路径
       dir = os.path.dirname(__file__)
       #top_dir = os.path.dirname(dir)
       #file_name = top_dir + "/pytest.ini"
       #file_name = dir + "/pytest.ini"
       file_name = dir + "/myapp.conf"
       #实例 ConfigParser
       self.config = configparser.ConfigParser()
       self.config.read(file_name,encoding='utf-8')

    def getconf(self, keyname):
       num = len(self.config.sections())
       i = 0
       print("num= ",num)
        #根据sections的数量进行循环查找keyname是否存在
       while i< num:
           section = self.config.sections()[i]
           #如果 keyname存在section中，则输出其参数值
           if keyname in self.config.options(section):
               pass
               # print("num-->", i)
               # print("section--->", section)
               # print("keyname--->", keyname)
               self.info = self.config.get(section, keyname)
               break
           else:
               i = i+1
       else:
           print("ReadConfig()没有找到config文件对应key")
       return self.info

if __name__ == "__main__":
    conf = ReadConfig()
    configinfo1 = conf.getconf("姓名")
    print(configinfo1)
    configinfo2 = conf.getconf("username")
    print( configinfo2 )
    configinfo3 = conf.getconf( "password" )
    print( configinfo3)


