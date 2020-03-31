import unicodedata
import hashlib

class dataStructure():
    def __init__(self):
        self.dict = {}

    def addSchema(self, data):
        data = unicodedata.normalize('NFKD', data).encode('ascii','ignore')
        hashid = hashlib.sha256(data).hexdigest()
        self.dict[hashid] = data
        return hashid

    def retrieveSchema(self, hashid):
        return self.dict[hashid]

