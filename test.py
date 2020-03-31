import requests

requestjson = """{'mytext':'lalala'}"""
requestcontent = {"mytext":"lalala"}

res = requests.post('http://localhost:9292/schemas', json=requestcontent)
print(res.headers, res.text, res.status_code)

hashid = res.json()['hash']
res = requests.get('http://localhost:9292/schemas/' + hashid)
print(res.headers, res.text, res.status_code)
print(requestjson)
