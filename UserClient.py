import datetime
from DataStore import DataS as ds
from datetime import timedelta

class UserClient:

    def __init__(self):
        self.dsObj = ds()

    def getInput(self):
        try:
            oper = int(input("Choose operation: \n1.create\n2.read\n3.delete"))
            if oper == 1:
                if self.dsObj.hasFileSizeExceed():
                    self.setOutput("Key value store size Exceeded")
                else:
                    keyName = str(input("Enter the key"))
                    if (self.dsObj.keyInList(keyName)):
                        self.setOutput("Key already exists")

                    else:
                        data = str(input("Write a value to the key:"))
                        ttlforfile =input('Do you want to set time to live for the key(if yes press "y"):')
                        expiretime = 0
                        if ttlforfile == 'y':
                            ttl = int(input("Enter the time to live for the key in seconds:"))
                            expiretime = datetime.datetime.now() + timedelta(seconds=ttl)
                            expiretime = expiretime.strftime("%d-%b-%Y (%H:%M:%S.%f)")
                        self.setOutput(self.dsObj.create(keyName, data, expiretime))


            if oper == 2:
                keyName = str(input("Enter the key"))
                readkeyval = self.dsObj.read(keyName)
                self.setOutput(readkeyval)

            if oper == 3:
                keyName = str(input("Enter the key"))
                deletekey = self.dsObj.delete(keyName)
                self.setOutput(deletekey)

        except ValueError:
            self.setOutput("Enter the correct value")

    def setOutput(self, result):
        print(result)
        chance=input("Do you want to continue the process (If yes press'y'):")
        if(chance=='y'):
            self.getInput()
        else:
            self.dsObj.writefile()
            print("Process completed")

uc = UserClient()
uc.getInput()
