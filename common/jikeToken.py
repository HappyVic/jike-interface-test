# -*- coding:utf-8 -*-
#!/usr/bin/python
import os
import getpathInfo

path = getpathInfo.get_Path()
token_path = os.path.join(path, 'token.txt')

def saveToken(token):
    jike_token = str(token)

    f = open(token_path, 'w')
    f.write(jike_token)
    f.close()

def getToken():
    f = open(token_path,'r')
    jike_token = eval(f.read())
    f.close()
    return jike_token
