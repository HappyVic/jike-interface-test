# --coding:utf-8--
# !/usr/bin/python
import os
import readConfig

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
    default_token = str({
        'x-jike-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiUnF0RG5MVFwvY2N2azdOemxaMnQ0Y1JKMXlwZ1dENzFkYjRcL1ZFbFp6R3B5UGR5SjJiWTZ0WnVxMU55XC9qZmN3UnJiMHpWQTgxZEsrUkJZaEpDa3luaFBVb1wvd2VSYTY4dGtXNWUyaWM0enBMYjdybVBHSzRyV2NNWW10bDJ6cVJCa2VFZENGa0JiRENvSGlGVEE0TFFZK0JFQnRzRHcxOU4xVXA5NWVSYXhRSE5PbzVZTk9vWjlNZTVRQjl2TXZRbjFpMTBBODdnTGI3OEkyYUtHdEhKTUJjdEw3M2JuZDN3ZnBsa2prS0pOczJweHVtWlNyeWhDMUtjQ0VUT1FGenpMUXpXSFJYRHdmK3lBK2ZsWlhXZFRJRXNyNmxrZXlqMUx1eUdoeitzS2EzNVd4TzkrUnVZdEJQbkk0WWdtalcyekErcERNOWlrWVZSZVwvR0F6Y1phcXcwOXRqU0ltQ0pOZVJqTmlHVk93ODJDWFJYSldXVnljVm12XC9adm1WbEdXZENxVjIxMVR4cml3YmtKNVo1b1Q5Zz09IiwidiI6MywiaXYiOiJWKzd2WVRhb09EQlJrY0NwSytKQTVnPT0iLCJpYXQiOjE1NTQxMjU5ODEuMjQ4fQ.GxeTiTDZjy_kIKTS-KSPh2gzYaNAOAJTXZ31dBK_8Tg',
        'x-jike-refresh-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjoiSGNEQmRZRWRGOUlqcDJXUXhnWlRUXC9YdG5SQU1yb0RxdlR1WE9oNFwvUkZlZVZHZklWMW1PcnpXV2NtOFVOaUEzRmdkUFM0WDhublJLODZCb0dxRE81eExUWUg5a0lEcG42YmtlSlJZa0pQR0wzUGNPNnRLMUptd2xBajdzZithUDNUZTNpVGRHTjZTV2krUlNpXC9GZTZvZlBTU3JaYW1jYnduMzJTMzVoUkxSalwvYkRBZnBhemRNVmZ2S1hncHAxU1wvT0ZRUDJVQ0xoeklIKzBRcERIWVR5UXQwK0Raa1JxZGxJbk9wQ3pUNnZBPSIsInYiOjMsIml2IjoiRmEzRDhBYWE2SHU2UUxCd3pwYXI0dz09IiwiaWF0IjoxNTU0MTI1OTgxLjI0OH0.dWxDN0mZvYQZ8g4UdPBNeiPU5xcZ0iOjAhxf61BHiks'})
    if not os.path.exists(token_path):
        with open(token_path, 'w') as f:
            f.write(default_token)
