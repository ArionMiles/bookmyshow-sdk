from bookmyshow.modules.base_module import BaseModule
from bookmyshow.modules.Fundamentals.events import Events


class Quickbook(BaseModule):
    def __init__(self, requester):
        super().__init__(requester)

    def get_movies(self, city_code, city_name, raw=False):
        request_headers = self.r.create_headers_from_rgn_code_and_name(city_code, city_name)
        data, headers = self.r.request(endpoint_name='quickbook', headers=request_headers, endpoint_format="MT")
        if raw:
            return data
        return Events(data, headers, self.r)
