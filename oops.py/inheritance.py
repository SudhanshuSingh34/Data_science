# Single inheritance in python 
class Employee:
    compony = "google"
    
    def showDetails(self):
        print (" thhis is the employee")
    
class programmer(Employee):
    language = "Pyhton"
    compony = "youtube"
    def getlanguage(self):
        print(f"the language is {self.language}")
    
    
    def showDetails(self):
        print (" this is the programmer")
 
e=Employee()  
e.showDetails() 
p = programmer()
p.showDetails()
print(p.language)
print(p.compony)

# Multiple inheritance in pythpn
class Employee:
    compony = "microsoft"
    level = 0
    
    def upgradeLevel(self):
        self.level = self.level + 1
        
class Worker:
    compony = "google"
    length = 10
    

class Programmer(Employee , Worker):
     width = 100
     
p = Programmer()
p.upgradeLevel()
print(p.compony)


# MultiLevel inheritance in python

class Person:
    country = "India"
    def takeBreath(self):
        print("i am breathing")
        
class Employee(Person):
    compony = "Hero"
    
    def upgradeLevel(self):
        print("level is updated")
        
    def takeBreath(self):
        print("i am breathing too")

class   Programmer(Employee):
    compony = "Cisco"  
    def getsalary(self):
        print("salary for this employee")      
    
        
p = Person()
p.takeBreath()
e = Employee()  
e.takeBreath()   
e.upgradeLevel()      
e.takeBreath()
Pr =Programmer()
Pr.takeBreath() 