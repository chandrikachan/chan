from abc import ABC
class parent:
    def message(self):
        pass
class A(parent):
    def message(self):
        print("this is first subclass")
class B(parent):
    def message(self):
        print("this is second subclass")
a1=parent()
a1.message()
b1=A()
b1.message()
c1=B()
c1.message()     
