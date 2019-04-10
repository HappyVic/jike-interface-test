import readConfig
import os
from xlrd import open_workbook
from common import configHttp
from common.Log import MyLog as Log
import json

localReadConfig = readConfig.ReadConfig()
testFilePath = os.path.join(readConfig.ProDir,'testFile')
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


def get_value_from_return_json(response_json, name1, name2):
    """
    get value by key
    :param response_json:
    :param name1:
    :param name2:
    :return:
    """
    group = response_json[name1]
    value = group[name2]
    return value

def get_value_dict_keys(dict):
    """
    :param dict:
    :return:
    """
    list = [i for i in dict]
    return list


def show_return_msg(response):
    """
    show msg detail
    :param response:
    :return:
    """
    url = response.url
    msg = response.text
    code=str(response.status_code)
    print("请求地址："+url)
    print("请求结果："+code)
    print("请求返回值："+'\n'+json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))
    # print('Response HTTP Response Body:', json.dumps(self.response.json(), indent=2, sort_keys=True, ensure_ascii=False))

    # indent: 缩进空格数，indent = 0输出为一行
    # sort_keys = True: 将json结果的key按ascii码排序
    # ensure_ascii = False: 不确保ascii码，如果返回格式为utf - 8包含中文，不转化为\u...
# ****************************** read testCase excel ********************************


def get_xls_case(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # 获取用例文件路径
    xls_path = os.path.join(testFilePath, 'case', xls_name)
    # 打开用例Excel
    file = open_workbook(xls_path)
    # 获得打开Excel的sheet
    sheet = file.sheet_by_name(sheet_name)
    # 获取这个sheet内容行数
    rows = sheet.nrows
    for i in range(rows):#根据行数做循环
        if sheet.row_values(i)[0] != u'case_name':#如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            cls.append(sheet.row_values(i))
    return cls

