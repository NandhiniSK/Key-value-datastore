import json
from DataStore import DataS as ds
import datetime
from datetime import timedelta

class TestCase:
    def __init__(self):
        self.dsObj=ds()
        self.testwithttl()
        self.testwithoutttl()
        self.testwithinvalidkey()
        self.testwithvalidkey()

    def testwithttl(self):
        self.tkey="file1"
        self.value="value1"
        self.tval=json.dumps('{"value":"' + self.value + '"}')
        self.tttl=1000
        self.expiretime = datetime.datetime.now() + timedelta(seconds=self.tttl)
        self.expiretime = self.expiretime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
        self.dsObj.create(self.tkey,self.value,self.expiretime)
        self.readval=self.dsObj.read(self.tkey)
        self.valueCheck()
        self.dsObj.delete(self.tkey)

    def testwithoutttl(self):
        self.tkey = "file2"
        self.value = "value2"
        self.tval = json.dumps('{"value":"' + self.value + '"}')
        self.expiretime = 0
        self.dsObj.create(self.tkey, self.value, self.expiretime)
        self.readval = self.dsObj.read(self.tkey)
        self.valueCheck()
        self.dsObj.writefile()

    def testwithinvalidkey(self):
        self.tkey = "file3"
        self.res=(self.dsObj.read(self.tkey))
        if(self.res=="No key found"):
            print("True")

    def testwithvalidkey(self):
        self.tkey = "file2"
        self.value="value2"
        self.tval = json.dumps('{"value":"' + self.value + '"}')
        self.res = (self.dsObj.read(self.tkey))
        self.valueCheck()

    def valueCheck(self):
        self.tval=json.loads(self.tval)
        print(self.tval==self.readval)

tc=TestCase()