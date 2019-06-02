import json
import datetime
import os

class DataS():

    def __init__(self):
        self.keylist = {}
        # Reads a json file and copy it to the global keylist
        with open('keyvalue-pair.json') as f:
            self.keylist = json.load(f)
        self.deleteExpiredKeys()

    def deleteExpiredKeys(self):
        dellist = []
        for key in self.keylist:
            listk = self.keylist[key]
            if listk[1] == 0:
                pass
            else:
                currenttime = (datetime.datetime.strptime(listk[1], '%d-%b-%Y (%H:%M:%S.%f)'))
                if (datetime.datetime.now() > currenttime):
                    dellist.append(key)
        for key in dellist:
            self.deletekey(key)

    def hasKeySizeExceeded(self,keyName):
        return (len(keyName)>32)

    def hasValueSizeExceed(self,value):
        return (len(value)>16000)

    def hasFileSizeExceed(self):
        filesize = os.path.getsize('keyvalue-pair.json')
        return (filesize > 1.024e+9)

    def create(self,keyName,value,expiretime,):
        self.deleteExpiredKeys()
        if self.keyInList(keyName):
             return ("Key already exists")
        else:
             if self.hasValueSizeExceed(value):
                    return ("Key size exceeded")
             else:
                    self.keylist[keyName] = []
                    data = json.dumps('{"value":"' + value + '"}')
                    self.keylist[keyName].append(data)
                    self.keylist[keyName].append(expiretime)
                    return ("Key added successfully")

    def keyInList(self,keyName):

        return (keyName in self.keylist.keys())

    def read(self,key):
        self.deleteExpiredKeys()
        if self.keyInList(key):
            listk = self.keylist[key]
            return (json.loads(listk[0]))
        else:
            return ("No key found")

    def delete(self,key):
        self.deleteExpiredKeys()
        if self.keyInList(key):
            self.deletekey(key)
            return "Key deleted successfully"
        else:
            return "No key found"

    def deletekey(self, key):

        del self.keylist[key]

    def writefile(self):
        with open('keyvalue-pair.json', 'w', encoding='utf-8') as newKey:
            json.dump(self.keylist, newKey)

