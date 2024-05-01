import httpx
import bs4
from FantaConverter import Convertify

class StringType(Convertify.String):
    ...

class FantaRespone(object):
    def __init__(self, url: str, proxies: dict = None,
                 cookies = None, headers = None, params = None):
        self.url = url
        self.prx = proxies
        self.cookies = cookies
        self.heads = headers
        self.params = params
        self.client = httpx.Client(proxies=self.prx, params=self.params, headers=self.heads, cookies=self.cookies)

    def get(self):
        try:
            resp = self.client.get(self.url)
            return {"local_error": False, "status_code": resp.status_code, "text": resp.text, "Object": resp}
        except Exception as E:
            return {"local_error": True, "error": str(E)}
        
    def post(self):
        try:
            resp = self.client.post(self.url)
            return {"local_error": False, "status_code": resp.status_code, "text": resp.text, "Object": resp}
        except Exception as E:
            return {"local_error": True, "error": str(E)}
        
    def patch(self):
        try:
            resp = self.client.patch(self.url)
            return {"local_error": False, "status_code": resp.status_code, "text": resp.text, "Object": resp}
        except Exception as E:
            return {"local_error": True, "error": str(E)}
        
    def put(self):
        try:
            resp = self.client.put(self.url)
            return {"local_error": False, "status_code": resp.status_code, "text": resp.text, "Object": resp}
        except Exception as E:
            return {"local_error": True, "error": str(E)}
        
    def delete(self):
        try:
            resp = self.client.delete(self.url)
            return {"local_error": False, "status_code": resp.status_code, "text": resp.text, "Object": resp}
        except Exception as E:
            return {"local_error": True, "error": str(E)}
        
    def getTag(self, tag: str | StringType):
        data = self.get().get('text')
        soup = bs4.BeautifulSoup(data, "html.parser")
        return Convertify.List().toList(soup.findAll(tag))