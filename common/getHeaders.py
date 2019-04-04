# -*- coding:utf-8 -*-
#!/usr/bin/python
import requests
import json
from common import jikeToken
import uuid
from random import choice
import string


def get_headers():
    """
    正式Headers
    :return:headers
    """
    access_token={
        "x-jike-access-token": jikeToken.get_token().get('x-jike-access-token')
    }
    headers = local_headers()
    headers.update(access_token)

    return headers


def local_headers():
    """
    本地Headers
    :return:Headers
    """
    headers = {
        "OS": "ios",
        "OS-Version": "Version 12.1.4 (Build 16D57)",
        "App-Version": "5.8.0",
        "App-BuildNo": "1314",
        "Manufacturer": "Apple",
        "Model": "iPhone11,6",
        "BundleID": "com.ruguoapp.jike",
        "x-jike-device-id": "20301BEB-4D1F-4F53-81A1-E187954819A5",
        "WifiConnected": "true",
        "King-Card-Status": "unknown",
        "Notification-Status": "OFF",
        "User-Agent": "%E5%8D%B3%E5%88%BB/1341 CFNetwork/976 Darwin/18.2.0",
        "Content-Type": "application/json; charset=utf-8",
    }
    return headers


def register_refresh_token():
    """
    注册刷新token保存到本地
    :return: 
    """
    #生成16位随机密码
    length = 16
    chars = string.ascii_letters + string.digits
    paw = ''.join([choice(chars) for i in range(length)])

    data = json.dumps({
                    "username": str(uuid.uuid4()).upper(),
                    "password": paw
                })

    try:
        response = requests.post(
            url="https://app-beta.jike.ruguoapp.com/1.0/users/register",
            headers=local_headers(),
            data=data
        )

        token = {
            "x-jike-access-token": response.headers.get('x-jike-access-token'),
            "x-jike-refresh-token": response.headers.get('x-jike-refresh-token')
        }
        jikeToken.save_token(token)
        return token

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def login_refresh_token():
    """
    登录刷新token保存到本地
    :return:
    """
    try:
        response = requests.post(
            url="https://app-beta.jike.ruguoapp.com/1.0/users/loginWithPhoneAndPassword",
            headers=local_headers(),
            data=json.dumps({
                "mobilePhoneNumber": "00000000001",
                "password": "111111",
                "areaCode": "+86"
            })
        )

        token = {
            "x-jike-access-token": response.headers.get('x-jike-access-token'),
            "x-jike-refresh-token": response.headers.get('x-jike-refresh-token')
        }
        jikeToken.save_token(token)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def refresh_tokens():
    """
    app_auth_tokens.refresh刷新token，保存到本地
    :return:
    """
    try:
        response = requests.post(
            url="https://app.jike.ruguoapp.com/1.0/app_auth_tokens.refresh",
            headers={
                "x-jike-device-id": "4DA0BE6A-69D6-4C3B-BCD3-A77310872F36",
                "x-jike-refresh-token": jikeToken.get_token().get('x-jike-refresh-token')
            },
        )

        token = {
            "x-jike-access-token": response.headers.get('x-jike-access-token'),
            "x-jike-refresh-token": response.headers.get('x-jike-refresh-token')
        }
        jikeToken.save_token(token)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

