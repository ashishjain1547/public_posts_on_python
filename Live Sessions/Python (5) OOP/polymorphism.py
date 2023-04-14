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

e = Engineer(who = 'Ashish', sal = 100)
e.getDetails()
e.reviseSalary()
e.getDetails()
e.reviseSalary(inc = 500)
e.getDetails()