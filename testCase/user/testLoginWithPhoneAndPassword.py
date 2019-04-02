import json
import unittest
import time
import paramunittest
from common import commontest
from common import configHttp as ConfigHttp

login_xls = commontest.get_xls_case("userCase.xlsx", "login")
configHttp = ConfigHttp.ConfigHttp()


@paramunittest.parametrized(*login_xls)
class TestLoginWithPhoneAndPassword(unittest.TestCase):
    def setParameters(self, case_name, method, mobilePhoneNumber, password, areaCode,):

        self.case_name = str(case_name)
        self.method = str(method)
        self.password = str(password)
        self.areaCode = str(areaCode)
        self.mobilePhoneNumber = str(mobilePhoneNumber)
        self.response = None

    def setUp(self):
        """

        :return:
        """
        print("开始测试用例"+self.case_name)

    def testLogin(self):
        """
        test body
        :return:
        """
        # set url
        self.url = commontest.get_url_from_xml('loginWithPhoneAndPassword')
        configHttp.set_url(self.url)
        print("第一步：设置url  "+self.url)

        #set headers
        configHttp.set_headers()
        print("第二步：设置headers" )

        # set date
        data = json.dumps({"mobilePhoneNumber":self.mobilePhoneNumber, "password":self.password,"reaCode":self.areaCode})
        configHttp.set_data(data)
        print("第三步：设置发送请求的参数")


        # test interface
        self.response = configHttp.post()
        print("第四步：发送请求\n\t\t请求方法：")



        print("第五步：检查结果")
        print('Response HTTP Status Code:', self.response.status_code)
        print('Response HTTP Response Body:', self.response.json())
        #print('Response HTTP Response Body:', json.dumps(self.response.json(), indent=2, sort_keys=True, ensure_ascii=False))
        # indent: 缩进空格数，indent = 0输出为一行
        # sork_keys = True: 将json结果的key按ascii码排序
        # ensure_ascii = Fasle: 不确保ascii码，如果返回格式为utf - 8包含中文，不转化为\u...

    def tearDown(self):
        time.sleep(2)
        print("测试结束，输出log完结\n\n")


if __name__ == "__main__":
    run = TestLoginWithPhoneAndPassword().testLogin()