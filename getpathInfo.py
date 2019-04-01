import os
from datetime import datetime

def get_Path():
    # 该文件的绝对路径
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


def get_resultPath(path):
    resultPath = os.path.join(path, "result")
    return resultPath



if __name__ == '__main__':  # 执行该文件，测试下是否OK
    print('测试路径是否OK,路径为：', get_logPath(get_resultPath(get_Path())))