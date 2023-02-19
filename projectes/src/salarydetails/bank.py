from abc import ABC
class bank(ABC):
    def getbalence(self,A,B,C):
        pass
class bankA:
    def getbalance(self):
        print("rs100 is deposited in BankA")
class bankB:
    def getbalance(self):
        print("rs150 is deposited BankB")
class bankC:
    def getbalance(self): 
        print("rs200 is deposited in BankC" )  
a=bankA()
a.getbalance()
b=bankB()
b.getbalance()
c=bankC()
c.getbalance()
