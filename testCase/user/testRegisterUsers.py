# -*- coding:utf-8 -*-
#!/usr/bin/python
# Install the Python Requests library:
# `pip install requests`

import requests
import json
import unittest
from common import getHeaders
import uuid
from random import choice
import string
from common import jikeToken

class RegisterUsers(unittest.TestCase):



    def test_gen_password(self):
        """
        生成16位随机密码
        :return: 返回密码
        """
        length=16
        chars = string.ascii_letters + string.digits
        paw=''.join([choice(chars) for i in range(length)])
        return paw



    def test_register_users(self):
        """
        post https://app.jike.ruguoapp.com/1.0/users/register
        :return:refresh_token
        """
        try:
            response = requests.post(
                url="https://app-beta.jike.ruguoapp.com/1.0/users/register",
                headers=getHeaders.GetHeaders.localHeaders(),
                data=json.dumps({
                    "username": str(uuid.uuid4()).upper(),
                    "password": RegisterUsers().test_gen_password()

                })
            )


            token={
                "x-jike-access-token":response.headers.get('x-jike-access-token'),
                "x-jike-refresh-token":response.headers.get('x-jike-refresh-token')
            }
            jikeToken.JikeToken().saveToken(token)
        except requests.exceptions.RequestException:
            print('HTTP1 Request failed')


if __name__ == '__main__':
      unittest.main()