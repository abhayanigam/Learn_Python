class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing....")

class Employee:
    company = "Honda"

    def getSalary(self):
        print("Salary is {}.".format(self.salary))

    def takeBreath(self):
        super().takeBreath()
        print("I am an employee so i am luckily breathing...")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print("No Salary to programmers")

    def takeBreath(self):
        
        print("I am a programmer breathing++..")

p = Person()
p.takeBreath()
#print(p.company) ---> Throws an error.

e = Employee()
e.takeBreath()

pr = Programmer()
pr.takeBreath()