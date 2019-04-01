# -*- coding:utf-8 -*-
#!/usr/bin/python
import json
import unittest
import time
import paramunittest
from common import commontest
from common import configHttp as ConfigHttp

smscode_xls = commontest.get_xls("userCase.xlsx", "smscode")
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*smscode_xls)
class TestGetSmsCode(unittest.TestCase):
    def setParameters(self, case_name, method, mobilePhoneNumber, areaCode, action, result, success):

        self.case_name = str(case_name)
        self.method = str(method)
        self.response = None
        self.areaCode = str(areaCode)
        self.result = str(result)
        self.mobilePhoneNumber = str(mobilePhoneNumber)
        self.action = str(action)
        self.success = bool(success)

    def setUp(self):
        """

        :return:
        """
        print("开始测试用例"+self.case_name)

    def testSmsCode(self):
        """
        test body
        :return:
        """
        # set url
        self.url = commontest.get_url_from_xml('getSmsCode')

        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        configHttp.set_headers()
        print("第二步：设置headers")


        # set date
        data = json.dumps({"mobilePhoneNumber":self.mobilePhoneNumber, "action":self.action,"reaCode":self.areaCode})
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")


        # test interface
        self.response = configHttp.post()
        print("第四步：发送请求\t\t请求方法："+self.method)


        print("第五步：检查结果")
        self.checkResult()
        #print('Response HTTP Response Body:', json.dumps(self.response.json(), indent=2, sort_keys=True, ensure_ascii=False))
        # indent: 缩进空格数，indent = 0输出为一行
        # sork_keys = True: 将json结果的key按ascii码排序
        # ensure_ascii = Fasle: 不确保ascii码，如果返回格式为utf - 8包含中文，不转化为\u...

    def tearDown(self):
        time.sleep(2)
        print("测试结束，输出log完结\n\n")


    def checkResult(self):
        """
        检查测试结果
        :return:
        """
        self.info = self.response.json()#返回json数据
        commontest.show_return_msg(self.response)#显示返回消息

        if  self.response.status_code == 200:

            if self.result == '1':
                action = commontest.get_value_from_return_json(self.info, 'data', 'action')
                self.assertEqual(self.info['success'], self.success)
                self.assertEqual(action, "LOGIN")
                self.assertEqual(self.response.status_code,200)




if __name__ == "__main__":
    run = TestGetSmsCode()