import urllib.request
import json

headers = {'Accept': 'application/json',
           'User-Agent': 'pythoncoursetest'}
req = urllib.request.Request('https://icanhazdadjoke.com',
                             headers=headers)
resp = urllib.request.urlopen(req)
data = resp.read()
jsonData = json.loads(data)
print(jsonData['joke'])
