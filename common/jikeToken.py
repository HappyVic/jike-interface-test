# --coding:utf-8--
# !/usr/bin/python
import os
import readConfig
from common import getHeaders

path = readConfig.ProDir  # 该文件的绝对路径
token_path = os.path.join(path, "token.txt")


def get_token():
    exists_file()
    with open(token_path, 'r') as f:
        jike_token = eval(f.read())
    return jike_token


def save_token(token):
    jike_token = str(token)
    with open(token_path, 'w') as f:
        f.write(jike_token)


def exists_file():
    if not os.path.exists(token_path):
        getHeaders.register_refresh_token()