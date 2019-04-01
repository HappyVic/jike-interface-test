
import readConfig
import os
from xml.etree import ElementTree as ET
from common import configHttp


localReadConfig = readConfig.ReadConfig()
proDir = readConfig.path
localConfigHttp = configHttp.ConfigHttp()





url_path = os.path.join(proDir, 'testFile', 'interfaceURL.xml')  # xml文件路径
tree = ET.parse(url_path)  # 将XMl文件加载并返回一个ELementTree对象

for u in tree.findall('url'): #查询url节点
    url_name = u.get('name')
    if url_name == "loginWithPhoneAndPassword":
        for i in u:
            print(i.text)

root = tree.getroot()
print(root.tag, "根属性", root.attrib)# 打印根元素的tag和属性

# 遍历xml文档的第二层
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag,"第二层", child.attrib)
    # 遍历xml文档的第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, "第三层", children.attrib)
        print(children.text+'第三层内容')