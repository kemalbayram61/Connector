from interfaces.HTTPMethods import HTTPMethods
from interfaces.ConnectorContentA import ConnectorContentA
import requests

class HTTPRequestConnector(ConnectorContentA):
    method:HTTPMethods = None
    url                = None
    data               = None
    def __init__(self, url, method, data=None):
        self.url    = url
        self.method = method
        self.data   = data

    def connect(self) ->bool:
        if(self.method == HTTPMethods.GET):
            request = requests.get(self.url)
            if(str(request.status_code) == "200"):
                return True
            return False
        elif(self.method == HTTPMethods.POST):
            request = requests.get(self.url)
            if(str(request.status_code) == "200"):
                return True
            return False
        elif(self.method == HTTPMethods.PUT):
            request = requests.get(self.url)
            if(str(request.status_code) == "200"):
                return True
            return False
        elif(self.method == HTTPMethods.DELETE):
            request = requests.get(self.url)
            if(str(request.status_code) == "200"):
                return True
            return False

    def run(self):
        if(self.method == HTTPMethods.GET):
            request = requests.get(self.url)
            if(str(request.status_code) == "200"):
                print(str(self.url) + " get success")
                return True
            print(str(self.url) + " status code " + str(request.status_code))
            return False
        elif(self.method == HTTPMethods.POST):
            request = requests.post(self.url, data=self.data)
            if(str(request.status_code) == "200"):
                print(str(self.url) + " post success")
                return True
            print(str(self.url) + " status code " + str(request.status_code))
            return False
        elif(self.method == HTTPMethods.PUT):
            request = requests.put(self.url, data=self.data)
            if(str(request.status_code) == "200"):
                print(str(self.url) + " put success")
                return True
            print(str(self.url) + " status code " + str(request.status_code))
            return False
        elif(self.method == HTTPMethods.DELETE):
            request = requests.delete(self.url)
            if(str(request.status_code) == "200"):
                print(str(self.url) + " delete success")
                return True
            print(str(self.url) + " status code " + str(request.status_code))
            return False