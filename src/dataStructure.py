import unicodedata
import hashlib

class dataStructure():
    def __init__(self):
        # make it private if possible
        self.dict = {}

    def addSchema(self, data):
        data = unicodedata.normalize('NFKD', str(data)).encode('ascii','ignore')
        hashid = hashlib.sha256(data).hexdigest()
        if hashid not in self.dict:
            self.dict[hashid] = data
        return hashid

    def retrieveSchema(self, hashid):
        return self.dict[hashid]

