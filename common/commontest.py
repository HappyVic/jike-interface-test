import requests
import readConfig
import getpathInfo
import os
from xlrd import open_workbook
from xml.etree import ElementTree as ET
from common import configHttp
from common.Log import MyLog as Log
import json

localReadConfig = readConfig.ReadConfig()
path = getpathInfo.get_Path()
localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.get_logger()

caseNo = 0


def get_visitor_token():
    """
    create a token for visitor
    :return:
    """
    host = localReadConfig.get_http("BASEURL")
    response = requests.get(host+"/v2/User/Token/generate")
    info = response.json()
    token = info.get("info")
    logger.debug("Create token:%s" % (token))
    return token


def set_visitor_token_to_config():
    """
    set token that created for visitor to config
    :return:
    """
    token_v = get_visitor_token()
    localReadConfig.set_headers("TOKEN_V", token_v)


def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    info = json['info']
    group = info[name1]
    value = group[name2]
    return value


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
    # sork_keys = True: 将json结果的key按ascii码排序
    # ensure_ascii = Fasle: 不确保ascii码，如果返回格式为utf - 8包含中文，不转化为\u...
# ****************************** read testCase excel ********************************



def get_value_from_return_json(json, name1, name2):
    """
    get value by key
    :param json:
    :param name1:
    :param name2:
    :return:
    """
    group = json[name1]
    value = group[name2]
    return value



def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # 获取用例文件路径
    xlsPath = os.path.join(path, "testFile", 'case', xls_name)
    # 打开用例Excel
    file = open_workbook(xlsPath)
    # 获得打开Excel的sheet
    sheet = file.sheet_by_name(sheet_name)
    # 获取这个sheet内容行数
    nrows = sheet.nrows
    for i in range(nrows):#根据行数做循环
        if sheet.row_values(i)[0] != u'case_name':#如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            cls.append(sheet.row_values(i))
    return cls

# ****************************** read SQL xml ********************************
database = {}


def set_xml():
    """
    set sql xml
    :return:
    """
    if len(database) == 0:
        sql_path = os.path.join(proDir, "testFile", "SQL.xml")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            # print(db_name)
            table = {}
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                sql = {}
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    # print(sql_id)
                    sql[sql_id] = data.text
                table[table_name] = sql
            database[db_name] = table


def get_xml_dict(database_name, table_name):
    """
    get db dict by given name
    :param database_name:
    :param table_name:
    :return:
    """
    set_xml()
    database_dict = database.get(database_name).get(table_name)
    return database_dict


def get_sql(database_name, table_name, sql_id):
    """
    get sql by given name and sql_id
    :param database_name:
    :param table_name:
    :param sql_id:
    :return:
    """
    db = get_xml_dict(database_name, table_name)
    sql = db.get(sql_id)
    return sql
# ****************************** read interfaceURL xml ********************************


def get_url_from_xml(name):
    url_path = os.path.join(path, 'testFile', 'interfaceURL.xml')  # xml文件路径
    tree = ET.parse(url_path)  # 将XMl文件加载并返回一个ELementTree对象

    for u in tree.findall('url'): #查询host节点
        url_name = u.get('name')
        if url_name == name:
            for i in u:
                return i.text

if __name__ == "__main__":
    print(get_url_from_xml('loginWithPhoneAndPassword'))


