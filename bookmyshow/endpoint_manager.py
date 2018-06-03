class EndpointManager:
    def __init__(self):
        self.base_url = "https://in.bookmyshow.com/serv"
        self.endpoints = self.get_endpoints()

    def get_endpoints(self):
        endpoints = {
            "quickbook": self.base_url + "/getData?cmd=quickbook&type={0}"
        }
        return endpoints

    def get_endpoint(self, name):
        return self.endpoints[name]
