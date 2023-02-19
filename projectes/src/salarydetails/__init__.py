class Member:
   def __init__(self, Name, Age, Phone_Number, Address, Salary):
       self.Name = Name
       self.Age = Age
       self.Phone_Number = Phone_Number
       self.Address = Address
       self.Salary = Salary
   def printSalary(self):
       print(self.Salary)
class Employee(Member):
   def __init__(self, specialization, Name, Age, Phone_Number, Address, Salary):
       self.specialization = specialization
       Member.__init__(self, Name, Age, Phone_Number, Address, Salary)
class Manager(Member):
   def __init__(self, department, Name, Age, Phone_Number, Address, Salary):
       self.department = department
       Member.__init__(self, Name, Age, Phone_Number, Address, Salary)
emp = Employee("Data Science", "manu", 23, 9000900022, "Hammond", 5500)
emp.printSalary()
mgr = Manager("Data Science", "Anu", 35, 9009009002, "Hammond", 11000)
mgr.printSalary()
       
