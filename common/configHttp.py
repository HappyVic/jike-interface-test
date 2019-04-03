import requests
import readConfig as readConfig
from common import getHeaders
from common.Log import MyLog as Log


localReadConfig = readConfig.ReadConfig()


class ConfigHttp():

    def __init__(self):
        global scheme, host, timeout
        scheme = localReadConfig.get_http("scheme")
        host = localReadConfig.get_http("baseurl")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.params = {}
        self.headers = None
        self.data = {}
        self.url = None


    def set_url(self, url):
        self.url = scheme +'://'+host+url


    def set_headers(self):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = getHeaders.get_headers()

    def set_loca_headers(self):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = getHeaders.local_headers()


    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

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
            response = requests.get(self.url, headers=self.headers, params=self.params ,data=self.data)
            if response.status_code == 200:
                return response
            elif response.status_code == 401:
                refresh_tokens()
                response = requests.get(self.url, headers=self.headers, params=self.params ,data=self.data)
                return response
            else:
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
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data)
            if response.status_code == 200:
                return response
            elif response.status_code == 401:
                refresh_tokens()
                response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data)
                return response
            else:
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
