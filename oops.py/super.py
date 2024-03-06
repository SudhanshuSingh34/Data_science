

class Person:
    country = "India"
    def __init__(self):
        print("this is person...\n")
        
    def takeBreath(self):
        print("i am breathing")
        
class Employee(Person):
    compony = "Hero"
    
    def __init__(self):
        super().__init__()
        print("this is employee...\n")
    
    def upgradeLevel(self):
        print("level is updated")
        
    def takeBreath(self):
        print("i am breathing too")

class   Programmer(Employee):
    compony = "Cisco" 
    
    def __init__(self):
        super().__init__()
        print("this is Programmer...\n") 
    def getsalary(self):
        print("salary for this employee")
        
    def takeBreath(self):
        print("i am breathing++")      
    
        
# p = Person()
# p.takeBreath()

# e = Employee()  
# e.takeBreath()       

Pr =Programmer()
# Pr.takeBreath() 