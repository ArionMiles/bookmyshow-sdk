import requests
from bookmyshow.endpoint_manager import EndpointManager
from bookmyshow.exceptions import *


class Requester(EndpointManager):
    def __init__(self):
        super().__init__()
        self.r = object

    def request(self, endpoint_name=None, method="GET", params=None, data=None,
                endpoint_format=None, raw_response=False, raw_url=None):
        if params is None:
            params = {}
        if data is None:
            data = {}
        if endpoint_format:
            raw_url = self.endpoints[endpoint_name]
            if isinstance(endpoint_format, str):
                url = raw_url.format(endpoint_format)
            else:
                url = raw_url.format(*endpoint_format)
        elif raw_url:
            url = raw_url
        else:
            url = self.endpoints[endpoint_name]
        self.r = requests.request(method, url, params=params, data=data)
        self.check_for_exceptions(self.r)
        if raw_response:
            return self.r
        return self.r.json(), self.r.headers

    @staticmethod
    def check_for_exceptions(request):
        status_code = request.status_code
        if status_code == 200:
            return
        elif status_code == 400:
            raise InvalidInputException("Invalid input")
        elif status_code == 404:
            raise NotFoundException("Not Found")
        else:
            raise ConnectionErrorException("The website couldn't be retrieved.")
