import requests
import readConfig as readConfig
from common import getHeaders
from common.Log import MyLog as Log


localReadConfig = readConfig.ReadConfig()


class ConfigHttp():

    def __init__(self):
        global scheme, host
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        self.headers = None
        self.data = {}
        self.url = None
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def set_url(self, url):
        self.url = scheme +'://'+host+url

    def set_headers(self):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = getHeaders.GetHeaders.getHeaders()


    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data


    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers,data=self.data)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include get params and post data
    # uninclude upload file
    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data)
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include upload file
    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # for json
    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
