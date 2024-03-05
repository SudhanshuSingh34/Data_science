class Employee:
    compony = "google"
    def getsalary(self):
        print (f"salary for this employee in {self.compony} is {self.salary}")
          
          
harry = Employee()
harry.salary = 100000
harry.getsalary() # Employee.getsalary(harry)
          