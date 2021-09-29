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

        if len(jsonData['joke']) > 10000:
            raise ValueError("fel eller")

        return jsonData['joke']
