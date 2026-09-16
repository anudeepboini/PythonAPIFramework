import requests

class APIClient:
    def get(self,url):
        return requests.get(url)
    def post(self,url,payload):
        return requests.post(url,json=payload)
    def put(self,url,payload):
        return requests.put(url,json=payload)
    def patch(self,url,payload):
        return requests.patch(url,json=payload)
    def delete(self,url):
        return requests.delete(url)