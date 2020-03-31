import requests
import json

data = {"mytext":"lalala"}

res = requests.post('http://localhost:9292/schemas', json=data)
print(res.headers, res.text, res.status_code)

hashid = res.json()['hash']
res = requests.get('http://localhost:9292/schemas/' + hashid)
print(res.headers, res.text, data)
rdata = json.loads(res.text)

assert rdata == data

