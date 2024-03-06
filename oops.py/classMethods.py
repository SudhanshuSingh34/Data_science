class Employee():
    country = "india"
    salary = 500
    location = "bihar"
    

    #instanceattributes
    # def changesalary(self, sal):
    #     self.salary = sal
 
    # def changesalary(self, sal):
           # self.__class__.salary = sal 
     
    @classmethod
    def  changesalary(cls , sal):
        cls.salary = sal
        
        
e = Employee
print(e.salary)
e.changesalary(1000)
print(e.salary)
print(Employee.salary)
