class Employee: # General superclass
    def __init__(self, who = "NA", sal = 0): # Set name when constructed
        self.name = who
        self.salary = sal

    def getDetails(self):
        rtn = (self.name, self.salary)
        print("rtn: ", rtn)
        return rtn

class Engineer(Employee): # Specialized subclass
   pass

"""
def __init__(self, who, sal): # Set name when constructed
    self.name = who
    self.salary = sal

e = Engineer()
Traceback (most recent call last):
  File "inheritance.py", line 14, in <module>
    e = Engineer()
TypeError: __init__() missing 2 required positional arguments: 'who' and 'sal'
"""

print("Defaults:")
e = Engineer()
e.getDetails()

print()
print("Custom:")
e = Engineer(who = 'Ashish', sal = '100')
e.getDetails()