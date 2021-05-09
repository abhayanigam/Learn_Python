class employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee.")

class programmer(employee):
    language = "Python"
    #company = "Youtube" ---> Over writing in the child class,so that this is going to be print.

    def getLanguage(self):
        print("The language is {}.".format(self.language))

    def showDetails(self): #this is overwriting in the inheritance.
        print("This is an programmer.")

e = employee()
e.showDetails()

p = programmer()
p.getLanguage()

p.showDetails()
print(p.company)