# -*- coding:utf-8 -*-
#!/usr/bin/python


import requests
import json
import unittest
from common import getHeaders
import time


class RecommendFeedList(unittest.TestCase):





    def test_post_recommendFeed_list(self):
        """
        recommendFeed/list
        POST https://app-beta.jike.ruguoapp.com/1.0/recommendFeed/list
        :return:
        """

        try:
            response = requests.post(
                url="https://app.jike.ruguoapp.com/1.0/recommendFeed/list",
                headers=getHeaders.get_headers(),
                data=json.dumps({
                    "limit": 10,
                    "trigger": "user"
                })
            )
            if response.status_code== 401:
                refresh_tokens()
                response= requests.post(
                    url="https://app.jike.ruguoapp.com/1.0/recommendFeed/list",
                    headers=getHeaders.get_headers(),
                    data=json.dumps({
                        "limit": 10,
                        "trigger": "user"
                    })
                )

            print('Response HTTP Status Code:',response.status_code)
            print('Response HTTP Response Body:',response.json())
            time.sleep(2)
        except requests.exceptions.RequestException:
            print('HTTP Request failed')

if __name__ == '__main__':
      unittest.main()