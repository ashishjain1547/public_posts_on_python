class Employee:
    def __init__(self, who = "NA", sal = 0): 
        self.name = who
        self.salary = sal

    def getDetails(self):
        rtn = (self.name, self.salary)
        print("rtn: ", rtn)
        return rtn

class Engineer(Employee): 
    def reviseSalary(self):
        self.salary =+ 100

    def reviseSalary(self, inc = 200):
        self.salary =+ inc

    def __str__(self): # Higher priority than __repr__ when using with print()
        return '[From __str__: %s, %s]' % (self.name, self.salary)

    #def __repr__(self):
    #    return '[From __repr__: %s, %s]' % (self.name, self.salary)

e = Engineer(who = 'Ashish', sal = 100)
e.getDetails()
e.reviseSalary()
e.getDetails()
e.reviseSalary(inc = 500)
e.getDetails()

print("e:", e)
print("e.__repr__():", e.__repr__())

f = Employee()
print("f = Employee():", f)