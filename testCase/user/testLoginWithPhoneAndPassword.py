import json
import unittest
import time
import paramunittest
from common.Log import MyLog
from common import commontest
from common import url
from common import configHttp
from common import jikeToken

login_xls = commontest.get_xls_case("userCase.xlsx", "login")
configHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*login_xls)
class TestLoginWithPhoneAndPassword(unittest.TestCase):
    def setParameters(self, case_name, method, mobilePhoneNumber, password, areaCode, result ,msg ,code):

        self.case_name = str(case_name)
        self.method = str(method)
        self.mobilePhoneNumber = str(mobilePhoneNumber)
        self.password = str(password)
        self.areaCode = str(areaCode)
        self.result = str(result)
        self.msg = str(msg)
        self.code = int(code)
        self.response = None

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        print("开始测试用例"+self.case_name)

    def testLogin(self):
        """
        test body
        :return:
        """
        # set url
        self.url = url.users_loginWithPhoneAndPassword
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        #set headers
        configHttp.set_headers()
        print("第二步：设置headers" )

        # set data
        data = json.dumps({"mobilePhoneNumber":self.mobilePhoneNumber, "password":self.password,"reaCode":self.areaCode})
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")


        # test interface
        self.response = configHttp.post()
        print("第四步：发送请求\n\t\t请求方法：")


        self.checkResult()
        print("第五步：检查结果")
        #print('Response HTTP Response Body:', json.dumps(self.response.json(), indent=2, sort_keys=True, ensure_ascii=False))
        # indent: 缩进空格数，indent = 0输出为一行
        # sork_keys = True: 将json结果的key按ascii码排序
        # ensure_ascii = Fasle: 不确保ascii码，如果返回格式为utf - 8包含中文，不转化为\u...

    def tearDown(self):
        time.sleep(1)
        if self.response.status_code == 200:
            token = {
                "x-jike-access-token": self.response.headers.get('x-jike-access-token'),
                "x-jike-refresh-token": self.response.headers.get('x-jike-refresh-token')
            }
            jikeToken.save_token(token)
        else:
            pass

        self.log.build_case_line(self.case_name, str(self.response))
        print("测试结束，输出log完结\n\n")


    def checkResult(self):
        """
        check test result
        :return:
        """
        self.info = self.response.json()
        # show return message
        commontest.show_return_msg(self.response)

        if self.result == '1':
            self.assertEqual(self.response.status_code, self.code)
            self.assertEqual(self.info['user']['screenName'], self.msg)

        if self.result == '0':
            self.assertEqual(self.response.status_code, self.code)
            self.assertEqual(self.info['error'], self.msg)



if __name__ == "__main__":
    unittest.main()