import urllib.request
import json


class DadService:
    def joke(self):
        headers = {'Accept': 'application/json',
                   'User-Agent': 'pythoncoursetest'}
        req = urllib.request.Request('https://icanhazdadjoke.com',
                                     headers=headers)
        resp = urllib.request.urlopen(req)
        data = resp.read()
        jsonData = json.loads(data)
        return jsonData['joke']
