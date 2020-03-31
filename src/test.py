import requests

data = {"mytext":"lalala"}

# adding data/posting data
res = requests.post('http://localhost:9292/schemas', json=data)

# retrieving data 
hashid = res.json()['hash']
res = requests.get('http://localhost:9292/schemas/' + hashid)

assert str(res.json()) == str(data)
print("pass")

# posting exactly the same data
res = requests.post('http://localhost:9292/schemas', json=data)
assert res.json()['hash'] == hashid
print("pass")